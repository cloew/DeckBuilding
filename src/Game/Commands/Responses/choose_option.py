
class ChooseOption:
    """ Represents a Command to choose an option """
    
    def __init__(self, option, owner):
        """ Initialize the Choose Option Command """
        self.option = option
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        self.owner.continueCommand(self.option)