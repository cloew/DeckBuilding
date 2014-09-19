
class StartTurn:
    """ Represents a Command to start the turn """
    
    def __init__(self, turn):
        """ Initialize the Command """
        self.turn = turn
        
    def perform(self):
        """ Perform the command """
        coroutine = self.turn.start()
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)