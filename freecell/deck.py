#!/usr/bin/env python3
"""
Module: deck
--------------------------
This module defines the Deck class, which is responsible for creating and managing
a collection of Card objects used in the Freecell game.
"""

from card import Card

class Deck:
    """
    Represents a deck of playing cards.
    
    Attributes:
        cards (list): A list of Card objects representing the deck.
    """
    
    def __init__(self):
        """
        Create a Deck instance and build the complete set of playing cards.
        """
        self.cards = []
        self._build_deck()
    
    def _build_deck(self):
        """
        Build a standard deck of 52 playing cards by combining all suits and ranks.
        """
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        """
        Shuffle the deck randomly.
        """
        import random
        random.shuffle(self.cards)
