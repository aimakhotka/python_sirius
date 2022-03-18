import tarfile, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', default='')
parser.add_argument('-o', '--output', default='archive.tar.gz')
args = parser.parse_args(sys.argv[1:])
print(args.output)

def archiving():
    arch_name = args.file.split('.')[0] + '.tar.gz'
    t = tarfile.open(arch_name, 'w|gz')
    t.add(args.file)
    t.close()

archiving()