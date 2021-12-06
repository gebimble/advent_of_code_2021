import numpy as np
from scipy import stats

from advent_of_code_2021.day_04 import numbers, bingo_cards

from pathlib import Path
from advent_of_code_2021.api.parsers.day04 import parse

def check_card(bingo_card: np.ndarray) -> bool:
    """check_card.

    Parameters
    ----------
    bingo_card : np.ndarray
        np.ndarray representing matches of a bingo card.

    Returns
    -------
    bool
        True if any row or column is all True in the matches array.

    """
    return any([any((bingo_card == True).all(axis=axis)) for axis in (0, -1)])

boolean_cards = [np.full_like(x, fill_value=False, dtype=bool) for x in bingo_cards]

def find_winner(numbers, bingo_cards, boolean_cards):
    for number in numbers:
        for i, card in enumerate(bingo_cards):
            if number in card:
                x = np.where(card == number)
                boolean_cards[i][x] = True

        for j, boolean_card in enumerate(boolean_cards):
            if check_card(boolean_card):
                return bingo_cards[j], boolean_card, number

winning_card, boolean_card, number = find_winner(numbers, bingo_cards, boolean_cards)
print(winning_card, boolean_card)
masked_array = np.ma.masked_array(winning_card, mask=boolean_card)
print(masked_array, masked_array.sum(), number)
print(masked_array.sum() * number)
