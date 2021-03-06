import kfp.dsl as dsl


@dsl.pipeline(
    name="VolumeSnapshotOp RokURL",
    description="The fifth example of the design doc."
)
def volume_snapshotop_rokurl(rok_url):
    vop1 = dsl.VolumeOp(
        name="create_volume_1",
        resource_name="vol1",
        size="1Gi",
        annotations={"rok/origin": rok_url},
        modes=dsl.VOLUME_MODE_RWM
    )

    step1 = dsl.ContainerOp(
        name="step1_concat",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["cat /data/file*| gzip -c >/data/full.gz"],
        pvolumes={"/data": vop1.volume}
    )

    step1_snap = dsl.VolumeSnapshotOp(
        name="create_snapshot_1",
        resource_name="snap1",
        volume=step1.pvolume
    )

    vop2 = dsl.VolumeOp(
        name="create_volume_2",
        resource_name="vol2",
        data_source=step1_snap.snapshot,
        size=step1_snap.outputs["size"]
    )

    step2 = dsl.ContainerOp(
        name="step2_gunzip",
        image="library/bash:4.4.23",
        command=["gunzip", "-k", "/data/full.gz"],
        pvolumes={"/data": vop2.volume}
    )

    step2_snap = dsl.VolumeSnapshotOp(
        name="create_snapshot_2",
        resource_name="snap2",
        volume=step2.pvolume
    )

    vop3 = dsl.VolumeOp(
        name="create_volume_3",
        resource_name="vol3",
        data_source=step2_snap.snapshot,
        size=step2_snap.outputs["size"]
    )

    step3 = dsl.ContainerOp(
        name="step3_output",
        image="library/bash:4.4.23",
        command=["cat", "/data/full"],
        pvolumes={"/data": vop3.volume}
    )


if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(volume_snapshotop_rokurl, __file__ + ".tar.gz")