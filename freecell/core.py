import enum
import itertools
import random


@enum.unique
class Value(enum.IntEnum):
    kA = 1
    k2 = 2
    k3 = 3
    k4 = 4
    k5 = 5
    k6 = 6
    k7 = 7
    k8 = 8
    k9 = 9
    k10 = 10
    kJ = 11
    kQ = 12
    kK = 13

    @property
    def code(self):
        return {Value.kA: "A"}


@enum.unique
class Suit(enum.Enum):
    SPADES = enum.auto()
    HEARTS = enum.auto()
    CLUBS = enum.auto()
    DIAMONDS = enum.auto()

    @property
    def code(self):
        if self == Suit.SPADES:
            return "\u2660"
        elif self == Suit.HEARTS:
            return "\u2665"
        elif self == Suit.CLUBS:
            return "\u2663"
        elif self == Suit.DIAMONDS:
            return "\u2666"
        else:
            raise ValueError


@enum.unique
class Color(enum.Enum):
    BLACK = enum.auto()
    RED = enum.auto()
    NONE = enum.auto()

    @property
    def code(self):
        if self == Color.BLACK:
            return "\x1b[1;30;47m"
        elif self == Color.RED:
            return "\x1b[1;31;47m"
        else:
            return "\x1b[0m"


class Card(object):
    def __init__(self, value=None, suit=None):
        if not value:
            value = Value.kA

        if not suit:
            suit = Suit.SPADES

        self.value = value
        self.suit = suit

    @property
    def color(self):
        if self.suit in [Suit.SPADES, Suit.CLUBS]:
            return Color.BLACK
        elif self.suit in [Suit.HEARTS, Suit.DIAMONDS]:
            return Color.RED
        else:
            return None

    def __repr__(self):
        val = f"{self.color.code}{self.value}{self.suit.code}{Color.NONE.code}"
        return val


class Foundation(object):
    def __init__(self, card=None):
        self.card = card


class Cell(object):
    def __init__(self, card=None):
        self.card = card


class Cascade(list):
    pass


class Board(object):
    def __init__(self):
        self.foundations = [Foundation() for _ in range(4)]
        self.cells = [Cell() for _ in range(4)]
        self.cascades = [Cascade() for _ in range(8)]

        deck = [Card(value, suit) for (value, suit) in itertools.product(Value, Suit)]
        random.shuffle(deck)

        for i, card in enumerate(deck):
            self.cascades[i % 8].append(card)
