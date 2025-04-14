#!/usr/bin/env python3
"""
Module: card
--------------------------
This module provides the Card class that represents an individual playing card
for the Freecell game. It encapsulates the card's suit and rank.
"""

class Card:
    """
    Represents a playing card with a suit and a rank.
    
    Attributes:
        rank (str): The rank of the card (e.g., 'A', '2', ..., 'K').
        suit (str): The suit of the card (e.g., 'hearts', 'diamonds', 'clubs', 'spades').
    """
    
    def __init__(self, rank, suit):
        """
        Initialize a Card instance.
        
        Args:
            rank (str): The rank of the card.
            suit (str): The suit of the card.
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Return a human-readable string representation of the card.
        
        Returns:
            str: The string representation (e.g., "A of hearts").
        """
        return f"{self.rank} of {self.suit}"
