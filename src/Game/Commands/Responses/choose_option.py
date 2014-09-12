
class ChooseOption:
    """ Represents a Command to choose an option """
    
    def __init__(self, option):
        """ Initialize the Choose Option Command """
        self.option = option
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.option)