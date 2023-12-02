import re

def filter_numbers(s):
    return re.sub(r'\D', '', s)

def dismantle_art(s):
    return int(s[0]+s[-1])

def convert_text_numbers(s):
    return re.sub('nine','n9e',
                  re.sub('eight','e8t',
                         re.sub('seven','s7n',
                                re.sub('six','s6x',
                                       re.sub('five','f5e',
                                              re.sub('four','f4r',
                                                     re.sub('three','t3e',
                                                            re.sub('two','t2o',
                                                                   re.sub('one','o1e',s)
                                                                   ))))))))

def solve(input):
    # part 1
    print(sum([dismantle_art(filter_numbers(line)) for line in input]))
    # part 2
    print(sum([dismantle_art(filter_numbers(convert_text_numbers(line))) for line in input]))