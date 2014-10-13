from Game.game import Game
from Game.player import Player
from Game.Card.card import Card
from Game.Card.Cost.fixed_cost import FixedCost
from Game.Card.VictoryPoints.fixed_points import FixedPoints
from Game.Characters.character import Character

from Game.Decks.deck_factory import DeckFactory

from kao_deck.deck import Deck

def BuildGame(**kwargs):
    """ Build a Card for testing purposes """
    return Game([BuildPlayer()], mainDeck=Deck(), superVillainDeck=BuildSuperVillainDeck())
    
def BuildPlayer(**kwargs):
    """ Build a Player for testing purposes """
    return Player("Test", BuildCharacter())

def BuildCard(**kwargs):
    """ Build a Card for testing purposes """
    return Card("Test", None, costCalculator=FixedCost(1), vpCalculator=FixedPoints(1), **kwargs)

def BuildCharacter():
    """ Build a Character for testing purposes """
    return Character("Test Character")

def BuildSuperVillainDeck():
    """ Build a Super Villain Deck for testing purposes """
    return DeckFactory.load("Super Villains").loadDeck()