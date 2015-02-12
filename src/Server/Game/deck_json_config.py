from kao_json import JsonAttr, KeywordAttr

from kao_deck.deck import Deck
from kao_deck.deck_with_discard_pile import DeckWithDiscardPile

def GetVisibleDeckKwargs(name, actionBuilders=[], includeActions=False):
    """ Returns if the quiz is for words """
    return {'hidden':False, 'name':name, 'actionBuilders':actionBuilders, 'includeActions':includeActions}

def GetDeckCards(deck, hidden):
    """ Returns if the quiz is for words """
    if hidden:
        return []
    else:
        return list(deck)
                           
deckConfig = [([Deck, DeckWithDiscardPile], [JsonAttr('count', lambda deck: len(deck)),
                                            KeywordAttr('hidden'),
                                            KeywordAttr('name'),
                                            JsonAttr('cards', GetDeckCards, args=['hidden'])
                                            ])]