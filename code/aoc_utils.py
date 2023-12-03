
# only remove unneccessary information here - further processing is done in day-scripts
def clean_line(line, day):
    if day == 1:
        return line.replace('\n','')
    if day == 2:
        return line.replace('\n','').replace(': ',':').replace('Game ','')
    if day == 3:
        return line.replace('\n','')

def read_input(path_base, day):
    path = path_base + str(day) + '.txt'
    with open(path,'r') as f:
        if day == 1:
            return [clean_line(line,day) for line in f.readlines()]
        if day == 2:
            return [clean_line(line,day) for line in f.readlines()]
        if day == 3:
            return [[c for c in clean_line(line, day)] for line in f.readlines()]
