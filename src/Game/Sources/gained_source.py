from list_source import ListSource

class GainedSource(ListSource):
    """ Represents the List of Gained Cards as a source """
    
    def __init__(self, cards, discardPileSource):
        """ Initialize the Source so that you can only interact 
            with Gained Cards that are in your discard pile """
        self.discardPileSource = discardPileSource
        discardPileSet = set(discardPileSource)
        ListSource.__init__(self, [card for card in cards if card in discardPileSet])
        
    def remove(self, card):
        """ Remove the given card """
        self.discardPileSource.remove(card)
        ListSource.remove(self, card)