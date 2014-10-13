from Game.Card.card_factory import CardFactory

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
        cardName = cardJson["name"]
        count = cardJson["count"]
        card = CardFactory.load(cardName)
        if card is None:
            print "Failed to load:", cardName
        deckInitializer.addItem(card, count)
    return deckInitializer

DECK_FILENAME = resource_manager.GetResourcePath("decks.json")

factories = {"REGULAR":Factory(Deck, [PrimitiveParameter("", optional=True), ComplexParameter("cards", LoadCards)]),
             "UNIFORM":Factory(Deck, [PrimitiveParameter("", optional=True), ComplexParameter("cards", LoadCards)]),
             "STARTING":Factory(DeckWithDiscardPile, [PrimitiveParameter("", optional=True), ComplexParameter("cards", LoadCards), PrimitiveParameter("reshuffle", optional=True, default=True)]),
             "FIXED_TOP":Factory(Deck, [PrimitiveParameter("", optional=True), ComplexParameter("cards", LoadCards)])}

DeckFactory = TypedDataSourceFactory('type', factories, JsonSource(DECK_FILENAME), "name")