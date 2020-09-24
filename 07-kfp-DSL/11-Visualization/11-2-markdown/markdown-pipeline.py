import kfp
from kfp import dsl

@dsl.pipeline(
    name = '11-2-markdown',
    description = 'Visulization'
)

def markdown_pipeline():
  pod = dsl.ContainerOp(
    name = 'markdown',
    image = 'hanjoo8821/markdown:ex',
    output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
  )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(markdown_pipeline, __file__ + '.tar.gz')