#!/usr/bin/env python3
"""dealer_bogus.py"""

from random import seed, randint

# fmt: off
suits: list[str] = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks: list[str] = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on


def init_deck() -> list[int]:
    """Returns a 52 element list of integers initialized from 0 to 51"""
    return list(range(52))


def card_name(card_num: int) -> str:
    """Returns the rank and suit for the given card number"""
    return f"{ranks[card_num % 13]} of {suits[card_num // 13]}"


def display_deck(deck: list[int]) -> None:
    """Displays each card in the given deck in order of increasing card position"""
    for card_pos, card_num in enumerate(deck):
        print(f"The card in position {card_pos} is the {card_name(card_num)}")


def deal_cards(deck: list[int]) -> None:
    """Sets each card position to a random card number between 0 and 51"""
    for card_pos, _ in enumerate(deck):
        new_card_num: int = randint(0, 51)
        deck[card_pos] = new_card_num


def main() -> None:
    seed(2016)
    deck: list[int] = init_deck()
    deal_cards(deck)
    display_deck(deck)


if __name__ == "__main__":
    main()
