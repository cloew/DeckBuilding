from Game.Card.card_factory import CardFactory

from deck_loader import DeckLoader
from shuffling_deck_loader import ShufflingDeckLoader
from starting_deck_loader import StartingDeckLoader
from fixed_top_card_deck_loader import FixedTopCardDeckLoader

from kao_deck.deck import Deck
from kao_deck.deck_initializer import DeckInitializer
from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

import resources.resource_manager as resource_manager

from kao_factory.factory import Factory
from kao_factory.typed_data_source_factory import TypedDataSourceFactory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

import json

def LoadCards(data):
    """ Load the Cards """
    deckInitializer = DeckInitializer()
    for cardJson in data:
        cardId = cardJson["id"]
        count = cardJson["count"]
        card = CardFactory.load(cardId)
        if card is None:
            print "Failed to load:", cardId
        deckInitializer.addItem(card, count)
    return deckInitializer

DECK_FILENAME = resource_manager.GetResourcePath("decks.json")

factories = {"REGULAR":Factory(ShufflingDeckLoader, [ComplexParameter("cards", LoadCards)]),
             "UNIFORM":Factory(DeckLoader, [ComplexParameter("cards", LoadCards)]),
             "STARTING":Factory(StartingDeckLoader, [ComplexParameter("cards", LoadCards)]),
             "FIXED_TOP":Factory(FixedTopCardDeckLoader, [ComplexParameter("cards", LoadCards), ComplexParameter("topCard", CardFactory.load)])}

DeckFactory = TypedDataSourceFactory('type', factories, JsonSource(DECK_FILENAME), "id")