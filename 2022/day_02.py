from enum import Enum

class PaperRockScissors():

    class Gesture(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    class MatchScores(Enum):
        LOSE = 0
        DRAW = 3
        WIN = 6

    _codes_to_gestures = {
        'A': Gesture.ROCK,
        'X': Gesture.ROCK,
        'B': Gesture.PAPER,
        'Y': Gesture.PAPER,
        'C': Gesture.SCISSORS,
        'Z': Gesture.SCISSORS,
    }

    def __init__(self, gesture_code: str) -> None:
        if gesture := PaperRockScissors._codes_to_gestures:
            self.gesture = PaperRockScissors._codes_to_gestures[gesture_code]
        else:
            raise ValueError(f'Gesture code {gesture_code} is not a valid paper, rock, scissors code')

    def get_score(self, other):
        if self.gesture == other.gesture:
            return self.gesture.value + PaperRockScissors.MatchScores.DRAW.value
        if (self.gesture == PaperRockScissors.Gesture.ROCK and other.gesture == PaperRockScissors.Gesture.SCISSORS) \
            or (self.gesture == PaperRockScissors.Gesture.PAPER and other.gesture == PaperRockScissors.Gesture.ROCK) \
            or (self.gesture == PaperRockScissors.Gesture.SCISSORS and other.gesture == PaperRockScissors.Gesture.PAPER):
            return self.gesture.value + PaperRockScissors.MatchScores.WIN.value
        else:
            return self.gesture.value + PaperRockScissors.MatchScores.LOSE.value

    def __str__(self) -> str:
        return f'{self.gesture.name}'


def parse_input(filename='day_02_input.txt'):
    # Parses the input file into a list of two-letters matches, e.g. ['AY', 'CZ', ...]
    with open(filename) as f:
        lines = [l for l in f.readlines() if l.strip()]
    lines = [l.strip().split() for l in lines]
    lines = [''.join(l) for l in lines]
    return lines

def part_1():
    games = parse_input()
    scores = 0
    for game in games:
        oponent_move = PaperRockScissors(game[0])
        my_move = PaperRockScissors(game[1])
        scores += my_move.get_score(oponent_move)
    return scores

def main():
    """
    >>> part_1()
    14375
    """
    print(part_1())
#    print(part_2())

main()
