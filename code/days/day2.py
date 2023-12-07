import days.base as base
from days.base import Basesolver

class Solver(Basesolver):

    def process_input(self, input):
        self.games = {}
        for game in input:
            game_id, rounds = game.split(':')
            self.games[int(game_id)] = [self.convert_to_dict(round) for round in self.split_rounds(rounds)]

    def solve_1(self):
        return sum([id for id in self.games if self.check_valid_game(self.games[id])])
    
    def solve_2(self):
        return sum([self.get_power(self.games[game]) for game in self.games])

    def split_rounds(self,rounds):
        return rounds.split('; ')

    def convert_to_dict(self,round):
        draws = round.split(', ')
        draw_dict = {}
        for draw in draws:
            colour_value_pair = draw.split(' ')
            draw_dict[colour_value_pair[1]] = int(colour_value_pair[0])
        return draw_dict

    def check_valid_game(self,game):
        # set max values
        max_values = {'red' : 12,
                    'green' : 13,
                    'blue' : 14}
        
        for round in game:
            for colour in max_values:
                try:
                    if round[colour] > max_values[colour]:
                        return False
                except KeyError:
                    pass
        return True

    def get_power(self,game):
        # init min values
        min_values = {'red' : 0,
                    'green' : 0,
                    'blue' : 0}
        
        for round in game:
            for colour in round:
                if min_values[colour] < round[colour]:
                    min_values[colour] = round[colour]
        
        return min_values['red']*min_values['green']*min_values['blue']