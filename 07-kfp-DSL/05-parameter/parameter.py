import kfp
from kfp import dsl
from kfp.dsl import PipelineParam

def flip_coin_op():
    return dsl.ContainerOp(
        name = 'Flip coin',
        image = 'python:alpine3.6',
        command = ['sh', '-c'],
        arguments  = ['python -c "import random; result = \'heads\' if random.randint(0,1) == 0 else \'tails\'; print(result)" | tee /tmp/output'],
        file_outputs = {'output': '/tmp/output'}
    )

def print_op(msg):
    return dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['echo', msg]
    )

@dsl.pipeline(
    name = 'kfp-05-parameter',
    description = 'parameter'
)

def condition_pipeline(predict : str = 'heads'):
    flip = flip_coin_op()
    result = flip.output
    with dsl.Condition(result == predict):
        print_op('YOU WIN')
    with dsl.Condition(result != predict):
        print_op('YOU LOSE')

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(condition_pipeline, __file__ + '.tar.gz')