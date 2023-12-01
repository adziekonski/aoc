def read_file(day, testing=False):
    filename = f'data/input_{day}'
    if testing:
        filename = f'data/test_{day}'
    f = open(filename, 'r')
    lines = [l.rstrip() for l in f.readlines()]
    return lines