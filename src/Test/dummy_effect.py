
class DummyEffect:
    """ Represents an effect for the purposes of testing """
    
    def __init__(self):
        """ Initialize the Dummy Effect """
        self.performed = False
    
    def perform(self, context):
        """ Perform the effect """
        self.performed = True