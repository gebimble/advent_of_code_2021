from pathlib import Path
from itertools import takewhile, dropwhile


def parse(input_file: Path) -> dict:

    bingo_cards = []

    with input_file.open('r') as f:

        numbers = [int(x) for x in f.readline().split(',')]

        cards = f.read()

        for card in cards.split('\n\n'):

            bingo_cards.append([[int(x) for x in line.strip().split()] for line in card.strip().split('\n')])


    return {
        'data':
            {
                'numbers': numbers,
                 'bingo_cards': bingo_cards,
            },
    }
