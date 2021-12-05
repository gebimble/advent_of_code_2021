from pathlib import Path
from itertools import takewhile, dropwhile


def parse(input_file: Path) -> dict:

    bingo_cards = []

    with input_file.open('r') as f:

        numbers = [int(x) for x in f.readline().split(',')]

        for line in f:
            drop = dropwhile(lambda x: not x.strip(), f)
            take = takewhile(lambda x: x.strip(), drop)

            bingo_cards.append([[int(x) for x in line.strip().split()] for line in take])

    return {
        'data':
            {
                'numbers': numbers,
                 'bingo_cards': bingo_cards,
            },
    }
