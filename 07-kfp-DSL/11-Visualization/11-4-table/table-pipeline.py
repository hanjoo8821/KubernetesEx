import kfp
from kfp import dsl

@dsl.pipeline(
    name = '11-4-table',
    description = 'Visulization'
)

def table_pipeline():
  pod = dsl.ContainerOp(
    name = 'table',
    image = 'hanjoo8821/table:ex',
    output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
  )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(table_pipeline, __file__ + '.tar.gz')