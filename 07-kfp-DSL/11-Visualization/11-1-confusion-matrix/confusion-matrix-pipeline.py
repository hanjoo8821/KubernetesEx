import kfp
from kfp import dsl

@dsl.pipeline(
    name = '11-1-confusion-matrix',
    description = 'Visulization'
)

def confusion_matrix_pipeline():
  pod = dsl.ContainerOp(
    name='confusion-matrix',
    image='hanjoo8821/confusion-matrix:ex',
    output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
  )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(confusion_matrix_pipeline, __file__ + '.tar.gz')