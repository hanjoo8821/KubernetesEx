import kfp
from kfp import dsl
from kubernetes.client.models import V1EnvVar

def print_env_op():
    return dsl.ContainerOp(
        name = 'Print',
        image = 'alpine:3.6',
        command = ['sh', '-c', 'echo $EX1']
    )

@dsl.pipeline(
    name = 'kfp-09-Env example',
    description = 'Use enviroment variables.'
)

def environment_pipeline():
    env_var = V1EnvVar(name = 'EX1', value = 'ENV variable - Tmax HyperData')
    print_env_op().add_env_variable(env_var)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(environment_pipeline, __file__ + '.tar.gz')