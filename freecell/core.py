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
        s = {
            Value.kA: "A",
            Value.k2: "2",
            Value.k3: "3",
            Value.k4: "4",
            Value.k5: "5",
            Value.k6: "6",
            Value.k7: "7",
            Value.k8: "8",
            Value.k9: "9",
            Value.k10: "10",
            Value.kJ: "J",
            Value.kQ: "Q",
            Value.kK: "K",
        }[self]
        return f"{s:>2}"

    def __add__(self, val: int):
        return Value(int(self) + val)


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

    @property
    def color(self) -> Color:
        if self in [Suit.SPADES, Suit.CLUBS]:
            return Color.BLACK
        elif self in [Suit.HEARTS, Suit.DIAMONDS]:
            return Color.RED
        else:
            return None


class Card(object):
    def __init__(self, value: Value = None, suit: Value = None):
        if not value:
            value = Value.kA

        if not suit:
            suit = Suit.SPADES

        self.value = value
        self.suit = suit

    @property
    def color(self) -> Color:
        return self.suit.color

    def __str__(self):
        val = f"{self.color.code}{self.value.code}{self.suit.code}{Color.NONE.code}"
        return val

    def __add__(self, val: int):
        return Card(val + 1, self.suit)


class Foundation(object):
    def __init__(self, card: Card = None):
        self.card = card


class Cell(object):
    def __init__(self, card: Card = None):
        self.card = card


class Cascade(list):
    pass


class Board(object):
    def __init__(self):
        self.foundations = dict([(suit, Foundation()) for suit in Suit])
        self.cells = [Cell() for _ in range(4)]
        self.cascades = [Cascade() for _ in range(8)]

        deck = [Card(value, suit) for (value, suit) in itertools.product(Value, Suit)]
        random.shuffle(deck)

        for i, card in enumerate(deck):
            self.cascades[i % 8].append(card)

    def is_valid_from_cascade(self, cascade: Cascade) -> bool:
        if len(cascade) == 0:
            return False
        
        return True
    
    def is_valid_from_cell(self, cell: Cell) -> bool:
        if cell.card is None:
            return False
        return True
    
    def is_valid_to_foundations(self, card: Card) -> bool:
        if self.foundations[card.suit].card is None:
            if card.value != Value.kA:
                return False

        if self.foundations[card.suit] + 1 != card:
            return False
        
        return True
    
    def is_valid_to_cell(self, cell: Cell) -> bool:
        return cell.card is None
    
    def is_valid_to_cascade(self, card: Card, cascade: Cascade) -> bool:
        if len(cascade) == 0:
            return True
        
        if card.color == cascade[-1].color and card.value + 1 == cascade[-1].value:
            return True
        
        return False

    def cell2foundations(self, cell: Cell):
        if not self.is_valid_from_cell(cell):
            raise ValueError
        
        card = cell.card

        if not self.is_valid_to_foundations(card):
            raise ValueError

        self.foundations[card.suit] = card
        cell.card = None

    def cascade2foundations(self, cascade: Cascade):
        if not self.is_valid_from_cascade(cascade):
            raise ValueError
        
        card = cascade[-1]

        if not self.is_valid_to_foundations(card):
            raise ValueError
        
        self.foundations[card.suit] = card
        cascade.pop(-1)
    
    def __repr__(self):
        def _prettify(val):
            return f'{str(val):>18s}' if val is not None else ' '*4
        # string length is crazy long because of color codes
        foundations_string = ' '.join([_prettify(self.foundations[suit].card) for suit in Suit])
        cell_string = ' '.join(_prettify(c.card) for c in self.cells)
        n = max([len(x) for x in self.cascades])
        cascadesT = [[ci[j] if j < len(ci) else None for ci in self.cascades] for j in range(n)]
        cascades_string = '\n'.join([' '.join([_prettify(card) for card in c]) for c in cascadesT])

        return f'{foundations_string} {cell_string}\n\n{cascades_string}'