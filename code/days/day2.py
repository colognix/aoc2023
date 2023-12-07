
def split_rounds(rounds):
    return rounds.split('; ')

def convert_to_dict(round):
    draws = round.split(', ')
    draw_dict = {}
    for draw in draws:
        colour_value_pair = draw.split(' ')
        draw_dict[colour_value_pair[1]] = int(colour_value_pair[0])
    return draw_dict

def check_valid_game(game):
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

def get_power(game):
    # init min values
    min_values = {'red' : 0,
                  'green' : 0,
                  'blue' : 0}
    
    for round in game:
        for colour in round:
            if min_values[colour] < round[colour]:
                min_values[colour] = round[colour]
    
    return min_values['red']*min_values['green']*min_values['blue']

# abstract the input further for computing
def prepare_input(input):
    games = {}
    for game in input:
        game_id, rounds = game.split(':')
        games[int(game_id)] = [convert_to_dict(round) for round in split_rounds(rounds)]
    return games

def solve(input):
    # prepare input
    games = prepare_input(input)
    
    # part 1
    print(sum([id for id in games if check_valid_game(games[id])]))
    # part 2
    print(sum([get_power(games[game]) for game in games]))
