from Game.Effects.effect_arguments import EffectArguments

class CardsEvent:
    """ Represents an Event to wrap an arbitrary number of cards """
    
    def __init__(self, cards, fromSource, args):
        """ Initialize the Cards Event with the cards and where they came from """
        self.cards = cards
        self.fromSource = fromSource
        
        self.args = EffectArguments(args.game, cards, event=self, player=args.player)
    
    def add(self, card):
        """ Add the card from the deck """
        self.fromSource.add(card)    
        
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