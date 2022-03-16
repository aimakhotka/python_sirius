import sys
print(sys.argv)

class SourceNotFound(Exception):
    pass

def check():
    args = sys.argv[1:]
    if '__source' in args:
        source_index = args.index('__source') + 1
        if source_index < len(args):
            return args[source_index]
    raise SourceNotFound

print(check())