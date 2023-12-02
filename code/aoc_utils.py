
def read_input(path, format):
    with open(path,'r') as f:
        if format == 'plain_lines':
            return [line.replace('\n','') for line in f.readlines()]
