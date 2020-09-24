import kfp
from kfp import dsl

@dsl.pipeline(
    name = '11-3-roc',
    description = 'Visulization'
)

def roc_pipeline():
  pod = dsl.ContainerOp(
    name = 'roc',
    image = 'hanjoo8821/roc-curve:ex',
    output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
  )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(roc_pipeline, __file__ + '.tar.gz')