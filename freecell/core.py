import enum

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

@enum.unique
class Suit(enum.Enum):
    SPADES = enum.auto()
    HEARTS = enum.auto()
    CLUBS = enum.auto()
    DIAMONDS = enum.auto()

@enum.unique
class Color(enum.Enum):
    BLACK = enum.auto()
    RED = enum.auto()

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
    