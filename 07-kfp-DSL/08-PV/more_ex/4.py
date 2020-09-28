import kfp
import kfp.dsl as dsl


@dsl.pipeline(
    name="VolumeSnapshotOp Sequential",
    description="The fourth example of the design doc."
)
def volume_snapshotop_sequential(url):
    vop = dsl.VolumeOp(
        name="create_volume",
        resource_name="vol1",
        size="1Gi",
        modes=dsl.VOLUME_MODE_RWM
    )

    step1 = dsl.ContainerOp(
        name="step1_ingest",
        image="google/cloud-sdk:279.0.0",
        command=["sh", "-c"],
        arguments=["mkdir /data/step1 && "
                   "gsutil cat %s | gzip -c >/data/step1/file1.gz" % url],
        pvolumes={"/data": vop.volume}
    )

    step1_snap = dsl.VolumeSnapshotOp(
        name="step1_snap",
        resource_name="step1_snap",
        volume=step1.pvolume
    )

    step2 = dsl.ContainerOp(
        name="step2_gunzip",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["mkdir /data/step2 && "
                   "gunzip /data/step1/file1.gz -c >/data/step2/file1"],
        pvolumes={"/data": step1.pvolume}
    )

    step2_snap = dsl.VolumeSnapshotOp(
        name="step2_snap",
        resource_name="step2_snap",
        volume=step2.pvolume
    )

    step3 = dsl.ContainerOp(
        name="step3_copy",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["mkdir /data/step3 && "
                   "cp -av /data/step2/file1 /data/step3/file3"],
        pvolumes={"/data": step2.pvolume}
    )

    step3_snap = dsl.VolumeSnapshotOp(
        name="step3_snap",
        resource_name="step3_snap",
        volume=step3.pvolume
    )

    step4 = dsl.ContainerOp(
        name="step4_output",
        image="library/bash:4.4.23",
        command=["cat", "/data/step2/file1", "/data/step3/file3"],
        pvolumes={"/data": step3.pvolume}
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(volume_snapshotop_sequential, __file__ + '.tar.gz')