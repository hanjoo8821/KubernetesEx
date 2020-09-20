import kfp
import kfp.dsl as dsl

@dsl.pipeline(
    name = "kfp-10-pipeline_with_sidecar", 
    description = "Add a sidecar to an operation."
)

def pipeline_with_sidecar(sleep_sec: int = 30):
    echo = dsl.Sidecar(
        name = "echo",
        image = "hashicorp/http-echo:latest",
        args = ['-text="This is a sidecar replying service"']
    )

    op1 = dsl.ContainerOp(
        name = "download",
        image = "busybox:latest",
        command = ["sh", "-c"],
        arguments = ["sleep %s; wget localhost:5678 -O /tmp/results.txt" % sleep_sec],  # sleep for X sec and call the sidecar and save results to output
        sidecars = [echo],
        file_outputs = {"downloaded": "/tmp/results.txt"}
    )

    op2 = dsl.ContainerOp(
        name = "echo",
        image = "library/bash",
        command = ["sh", "-c"],
        arguments = ["echo %s" % op1.output]
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline_with_sidecar, __file__ + '.tar.gz')