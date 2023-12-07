import re
from days.base import Basesolver

class Solver(Basesolver):

       def solve_1(self):
              return sum([self.dismantle_art(self.filter_numbers(line)) for line in self.input])
       
       def solve_2(self):
              return sum([self.dismantle_art(self.filter_numbers(self.convert_text_numbers(line))) for line in self.input])
    
       def filter_numbers(self,s):
              return re.sub(r'\D', '', s)

       def dismantle_art(self,s):
              return int(s[0]+s[-1])

       def convert_text_numbers(self,s):
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