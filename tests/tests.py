import unittest

from .context import freecell

class TestValue(unittest.TestCase):
    def test_number_of_values(self):
        self.assertEqual(len([x for x in freecell.Value]), 13)

class TestSuit(unittest.TestCase):
    def test_number_of_values(self):
        self.assertEqual(len([x for x in freecell.Suit]), 4)

class TestCard(unittest.TestCase):
    def test_color_match_suit_as(self):
        value = freecell.Value.kA
        suit = freecell.Suit.SPADES
        expected_color = freecell.Color.BLACK
        self.check_color_match_suit(value, suit, expected_color)
    
    def test_color_match_suit_kh(self):
        value = freecell.Value.kK
        suit = freecell.Suit.HEARTS
        expected_color = freecell.Color.RED
        self.check_color_match_suit(value, suit, expected_color)

    def test_color_match_suit_qc(self):
        value = freecell.Value.kQ
        suit = freecell.Suit.CLUBS
        expected_color = freecell.Color.BLACK
        self.check_color_match_suit(value, suit, expected_color)
    
    def test_color_match_suit_jd(self):
        value = freecell.Value.kJ
        suit = freecell.Suit.DIAMONDS
        expected_color = freecell.Color.RED
        self.check_color_match_suit(value, suit, expected_color)

    def check_color_match_suit(self, value, suit, expected_color):
        card = freecell.Card(value, suit)
        self.assertEqual(card.color, expected_color)