import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', default='home/user')
args = parser.parse_args(sys.argv[1:])
print(args.output)