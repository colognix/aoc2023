from days.base import Basesolver
import numpy as np

class Solver(Basesolver):

    def process_input(self,input):
        self.pipe_plan = np.array(input)
        start_position = np.where(self.pipe_plan == 'S')
        self.start_position = (start_position[0][0],start_position[1][0])

    def set_constants(self):
        self.pipe_dict = {
            '|' :  {'s':'s','n':'n'} ,
            '-' :  {'e':'e','w':'w'} ,
            'L' :  {'s':'e','w':'n'} ,
            'J' :  {'s':'w','e':'n'} ,
            '7' :  {'e':'s','n':'w'} ,
            'F' :  {'w':'s','n':'e'}
        }

        self.dir_dict = {
            's' : (1,0),
            'n' : (-1,0),
            'e' : (0,1),
            'w' : (0,-1)
        }

    def solve_1(self):
        direction = self.find_start_directions(self.start_position)[0]
        position = self.start_position
        self.loop = np.zeros(self.pipe_plan.shape)
        self.loop_bloat = np.ones((self.pipe_plan.shape[0]*2+1,self.pipe_plan.shape[1]*2+1))
        self.loop[position] = 1
        self.path = []
        distance = 0
        bloat_start = self.get_dup_position(position)
        self.loop_bloat[bloat_start] = 2
        self.loop_bloat[self.get_next_position(bloat_start,direction)] = 2
        while True:

            try:
                position = self.get_next_position(position, direction)
                direction = self.pipe_dict[self.pipe_plan[position]][direction]
                distance += 1
                self.loop[position] = 1
                self.loop_bloat[self.get_dup_position(position)] = 2
                self.loop_bloat[self.get_next_position(self.get_dup_position(position),direction)] = 2
                self.path += [position]
            except KeyError:
                break
        self.loop_bloat[1:,1:] = self.loop_bloat[:-1,:-1]
        return int((distance+1)/2) 
    
    def solve_2(self):
        self.loop_bloat[0][:] = 0
        found_next = True
        while found_next:
            found_next = False
            for i in range(self.loop_bloat.shape[0]):
                for j in range(self.loop_bloat.shape[1]):
                    if self.loop_bloat[i][j] == 1:
                        if (self.loop_bloat[max(0,i-1):i+2,max(0,j-1):j+2] == 0).any() :
                            self.loop_bloat[i][j] = 0
                            found_next = True
        self.loop_bloat[:-1,:-1] = self.loop_bloat[1:,1:]
        return int(np.sum(np.mod(self.loop_bloat[::2,::2],2)))

    def get_start_shape(self):
        dirs = self.find_start_directions(self.start_position)
        for pipe in self.pipe_dict:
            if dirs == list(self.pipe_dict[pipe].values()):
                return pipe


    def get_next_position(self,position,dir):
        return tuple(map(lambda i, j: i + j, position, self.dir_dict[dir]))
    
    def get_dup_position(self,position):
        return tuple(map(lambda i: 2*i,position))

    def find_start_directions(self,position):
        dirs = []
        for dir in self.dir_dict:
            try:
                if dir in self.pipe_dict[self.pipe_plan[self.get_next_position(position,dir)]]:
                    dirs += [dir]
            except KeyError:
                continue
        return dirs