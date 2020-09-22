import kfp
from kfp import dsl

def flip_coin_op():
    return dsl.ContainerOp(
        name = 'Flip coin',
        image = 'python:alpine3.6',
        command = ['sh', '-c'],
        arguments = ['python -c "import random; result = \'heads\' if random.randint(0,1) == 0 else \'tails\'; print(result)" | tee /tmp/output'],    # Artifact
        file_outputs = {'output': '/tmp/output'}
    )

def print_op(message):
    return dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['echo', message]
    )
    
@dsl.pipeline(
    name = 'kfp-01-sequential',
    description = 'Coin Flip example : step.'
)

def seq_pipeline():
    flip = flip_coin_op()
    
    result = flip.output
    print_op(result)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(seq_pipeline, __file__ + '.tar.gz')