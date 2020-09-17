import kfp
from kfp import dsl

def flip_coin_op():
    return dsl.ContainerOp(
        name = 'Flip coin',
        image = 'python:alpine3.6',
        command = ['sh', '-c'],
        arguments = ['python -c "import json; import sys; import random; json.dump([(\'heads\' if random.randint(0,1) == 1 else \'tails\') for i in range(10)], open(\'/tmp/output.json\', \'w\'))"'],
        file_outputs = {'output': '/tmp/output.json'}
    )

def print_op(message):
    return dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['echo', message]
    )
    
@dsl.pipeline(
    name = 'kfp-03-loop',
    description = 'Coin Flip example : Parallel Loop'
)

def condition_pipeline():
    flip = flip_coin_op()
    
    result = flip.output
    
    with dsl.ParallelFor(result) as item:
        print_op(item)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(condition_pipeline, __file__ + '.tar.gz')
