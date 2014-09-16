from Game.Effects.effect_arguments import EffectArguments

class TopCardEvent:
    """ Represents an Event for Playing a Card """
    
    def __init__(self, card, fromSource, game):
        """ Initialize the Top Card Event with the card """
        self.cards = [card]
        self.game = game
        self.fromSource = fromSource
        
        self.args = EffectArguments(game, card, event=self)
        
    def remove(self, card):
        """ Remove the card from the deck """
        self.fromSource.remove(card)
        
    def __getitem__(self, index):
        """ Return the item at the given index """
        return self.cards[index]
        
    def __len__(self):
        """ Return the length of the event """
        return len(self.cards)
        
    def __iter__(self):
        """ Return the iterator for the event when it is used as a source """
        return self.cards.__iter__()