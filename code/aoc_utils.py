
# only remove unneccessary information here - further processing is done in day-scripts
def clean_line(line, day):
    # linebreaks
    line = line.replace('\n','')
    if day == 2:
        line = line.replace(': ',':').replace('Game ','')
    elif day == 4:
        line = line.replace('  ',' ').replace(' | ','|').split(':')[1][1:]
    elif day == 6:
        line = line.split(':')[1].split()
    elif day == 7:
        line = line.split()
        line = [line[0],int(line[1])]
    return line

def read_input(path_base, day):
    path = path_base + str(day) + '.txt'
    with open(path,'r') as f:
        if day == 3:
            return [[c for c in clean_line(line, day)] for line in f.readlines()]
        else:
            return [clean_line(line,day) for line in f.readlines()]
