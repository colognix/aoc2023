
# basic formatting
def prepare_line(line, day):
    # remove linebreaks (windows..)
    line = line.replace('\n','')

    # remove redundant trailing info followed by ':'
    if day in [4,6]:
        line = line.split(':')[1]

    # matrix
    if day in [3]:
        line = [c for c in line]
    # whitespace seperated values
    elif day in [6,7]:
        line = line.split()
        
    # key-value like line [str,int]
    if day in [7]:
        line = [line[0],int(line[1])]

    return line

def read_input(path_base, day):
    path = path_base + str(day) + '.txt'
    with open(path,'r') as f:
        return [prepare_line(line,day) for line in f.readlines()]
