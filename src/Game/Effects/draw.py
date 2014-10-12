from Game.Events.draw_card_event import DrawCardEvent

class Draw:
    """ Represents an effect to Draw Cards """
    
    def __init__(self, count=1):
        """ Initialize the Effect with the number of cards to draw """
        self.count = count
        
    def perform(self, context):
        """ Perform the Game Effect """
        context.player.draw(count=self.count)
        
        coroutine = context.owner.ongoingEffects.send(DrawCardEvent(context.parent, context.game))
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)