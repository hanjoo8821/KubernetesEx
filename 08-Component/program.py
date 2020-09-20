import argparse
from pathlib import Path

def do_work(input1_file, output1_file, param1):
    for x in range(param1):
        line = next(input1_file)
        if not line:
            break
        _ = output1_file.write(line)

parser = argparse.ArgumentParser(description = 'Program description')
parser.add_argument('--input-path', type = str, help = 'Path of the local file containing the Input data.')
parser.add_argument('--param', type = int, default = 100, help = 'Parameter.')
parser.add_argument('--output-path', type = str, help = 'Path of the local file where the Output data should be written.')
args = parser.parse_args()

Path(args.output1_path).parent.mkdir(parents=True, exist_ok=True)

with open(args.input1_path, 'r') as input1_file:
    with open(args.output1_path, 'w') as output1_file:
        do_work(input1_file, output1_file, args.param1)