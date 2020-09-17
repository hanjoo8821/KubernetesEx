import kfp
from kfp import dsl

@dsl.pipeline(
    name = 'ML pipeline - MNIST',
    description = 'Simple Machine Learning pipeline'
)

def ml_pipeline():
    dsl.ContainerOp(
        name = 'mnist-kfp',
        image = 'hanjoo8821/mnist-kfp:metrics',
        output_artifact_paths={'mlpipeline-metrics': '/mlpipeline-metrics.json'}
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ml_pipeline, __file__ + '.tar.gz')