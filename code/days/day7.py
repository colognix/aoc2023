from itertools import groupby
from days.base import Basesolver

class Solver(Basesolver):

    def set_constants(self):
        self.types = ['1','2','22','3','H','4','5']

    def set_part(self, part):
        self.part = part
        if part == 1:
            self.map_dict = {'A':'A','K':'B','Q':'C','J':'D','T':'E','9':'F','8':'G','7':'H','6':'I','5':'J','4':'K','3':'L','2':'M'}
        if part == 2:
            self.map_dict = {'A':'A','K':'B','Q':'C','J':'N','T':'E','9':'F','8':'G','7':'H','6':'I','5':'J','4':'K','3':'L','2':'M'}
        

    def solve(self):
        game_dict = self.create_game_dict()
        winnings = 0
        i = 0
        # for each type (ascending in strength)
        for t in self.types:
            try:
                # for each corresponding hand (ascending in strength)
                for hand in reversed(sorted(game_dict[t].keys(),key=self.card_order)):
                    i += 1
                    winnings += i*game_dict[t][hand]
            except KeyError:
                pass
        return winnings

    # get the type of hand
    def get_type(self,hand):
        splits = [len(list(g)) for k, g in groupby(sorted(hand))]
        # number of distinct cards
        num_splits = len(splits)
        # maximum number of same cards
        max_splits = max(splits)   

        if num_splits == 1:
            return '5'

        num_jokers = hand.count('J')
        if self.part == 2:
            # maximum number of same cards excluding jokers
            max_splits = max([len(list(g)) for k, g in groupby(sorted(hand)) if k != 'J'])

        # two distinct cards
        if num_splits == 2:
            # one (non-joker) with count 4
            if max_splits == 4:
            
                if (self.part == 2) & (num_jokers > 0):
                    return '5'
                else:
                    return '4'
            # one (non-joker with count 3)
            elif max_splits == 3:
                # if other distinct card is joker
                if (self.part == 2) & (num_jokers > 0):
                    return '5'
                else:
                    return 'H'
            # non-joker with count 2 -> joker has count 3
            else:
                return '5'
            
        # three distinct cards
        if num_splits == 3:
            # one non-joker with count 3
            if max_splits == 3:
                # other cards max count = 1
                if (self.part == 2) & (num_jokers == 1):
                    return '4'
                else:
                    return '3'
            # one non-joker with count 2 -> 2 pair, maybe one of them joker
            elif max_splits == 2:
                # single joker
                if (self.part == 2) & (num_jokers == 1):
                    return 'H'
                # double joker
                elif (self.part == 2) & (num_jokers == 2):
                    return '4'
                else:
                    return '22'
            # max 1 for non joker -> joker = 3
            else:
                return '4'
            
        # four distinct cards
        if num_splits == 4:
            # may be one or two jokers
            if (self.part == 2) & (num_jokers >= 1):
                return '3'
            else:
                return '2'
            
        # five distinct cards
        else:
            # max 1 joker
            if (self.part == 2) & (num_jokers == 1):
                return '2'
            else:
                return '1'

    # mapper function for ordering (char-based)
    def card_mapper(self,s):
        return self.map_dict[s]

    # hmapper function for ordering (string-based)
    def card_order(self,hand):
        return ''.join(list(map(self.card_mapper, hand)))

    # create a dictionary for iterating through types / ordered hands (by strength) for each type
    def create_game_dict(self):
        game_dict = {}
        for hand_and_bid in self.input:
            try:
                game_dict[self.get_type(hand_and_bid[0])][hand_and_bid[0]] = hand_and_bid[1]
            except KeyError:
                game_dict[self.get_type(hand_and_bid[0])] = {}
                game_dict[self.get_type(hand_and_bid[0])][hand_and_bid[0]] = hand_and_bid[1]
        return game_dict