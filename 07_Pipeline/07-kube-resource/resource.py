import kfp
from kfp import dsl
import json

_job_manifest = """
{
    "apiVersion": "batch/v1",
    "kind": "Job",
    "metadata": {
        "generateName": "kfp"
    },
    "spec": {
        "template": {
            "metadata": {
                "name": "resource-pipeline"
            },
            "spec": {
                "containers": [{
                    "name": "hell",
                    "image": "hanjoo8821/mnist-kfp:simple",
                    "command": ["python", "/app/ml-mnist.py"]
                }],
                "restartPolicy": "Never"
            }
        }   
    }
}
"""

@dsl.pipeline(
    name = 'kfp-07-Kubernetes Resource',
    description = 'A pipeline with resource.'
)

def resource_pipeline():
    op = dsl.ResourceOp(
        name = 'resource-job',
        k8s_resource = json.loads(_job_manifest),
        action = 'create'
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(resource_pipeline, __file__ + '.tar.gz')