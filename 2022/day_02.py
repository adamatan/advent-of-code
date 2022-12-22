def get_normalized_input(filename='day_02_input.txt'):
    # Parses the input file into a list of two-letters matches, e.g. ['AY', 'CZ', ...]
    with open(filename) as f:
        lines = [l for l in f.readlines() if l.strip()]
        lines = [l.strip().split() for l in lines]
        lines = [''.join(l) for l in lines]
    return lines

def calculate_game_score(two_letters_game):
    shape_values = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    shape_normalization = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    scores = {
        'lose': 0,
        'draw': 3,
        'win': 6
    }
    oponent_move, my_move = two_letters_game
    my_move = shape_normalization[my_move]

    if oponent_move == my_move:
        score = shape_values[my_move] + scores['draw']
        print(f'Draw {two_letters_game} {oponent_move} {my_move} {score}')
        return score
    if oponent_move+my_move in ('AB', 'BC', 'CA'):
        score = shape_values[my_move] + scores['win']
        print(f'Win  {two_letters_game} {oponent_move} {my_move} {score}')
        return score
    else:
        score = shape_values[my_move] + scores['lose']
        print(f'Lose {two_letters_game} {oponent_move} {my_move} {score}')
        return score


def part_1():
    games = get_normalized_input()
    scores = [calculate_game_score(game) for game in games]
    return sum(scores)


def main():
    print(part_1())
#    print(part_2())

main()
