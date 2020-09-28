import kfp.dsl as dsl


@dsl.pipeline(
    name="VolumeOp Parallel",
    description="The first example of the design doc."
)
def volumeop_parallel():
    vop = dsl.VolumeOp(
        name="create_pvc",
        resource_name="my-pvc",
        size="10Gi",
        modes=dsl.VOLUME_MODE_RWM
    )

    step1 = dsl.ContainerOp(
        name="step1",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo 1 | tee /mnt/file1"],
        pvolumes={"/mnt": vop.volume}
    )

    step2 = dsl.ContainerOp(
        name="step2",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo 2 | tee /common/file2"],
        pvolumes={"/common": vop.volume}
    )

    step3 = dsl.ContainerOp(
        name="step3",
        image="library/bash:4.4.23",
        command=["sh", "-c"],
        arguments=["echo 3 | tee /mnt3/file3"],
        pvolumes={"/mnt3": vop.volume}
    )


if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(volumeop_parallel, __file__ + ".tar.gz")