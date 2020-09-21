import kfp
from kfp import dsl

@dsl.pipeline(
    name = 'ML-02-artifact',
    description = 'Simple Machine Learning pipeline with artifacts'
)

def ml_pipeline():
    dsl.ContainerOp(
        name = 'mnist-kfp',
        image = 'hanjoo8821/mnist:artifact',
        output_artifact_paths={'mlpipeline-metrics': '/mlpipeline-metrics.json'}
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ml_pipeline, __file__ + '.tar.gz')