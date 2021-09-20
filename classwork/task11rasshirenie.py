fname = input()
def get_format(fname):
    l = fname.split('.')
    if len (l) < 2:
        return 'invalid'
    else:
        return l[-1]
print (get_format(fname))