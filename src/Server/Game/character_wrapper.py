from json_helper import GetActivatableActionJSON
from Game.Sources.source_factory import CHARACTER

class CharacterWrapper:
    """ ADD CLASS DESCRIPTION """
    CHARACTER_IMAGES_DIRECTORY_URL = 'static/images/Characters/'
    
    def __init__(self, character, game):
        """ Initialize the Card Wrapper """
        self.character = character
        self.game = game
        
    def toJSON(self):
        """ Return the card as a JSON Dictionary """
        actions = []
        activatableJSON = GetActivatableActionJSON(self.character, self.game, source=CHARACTER)
        if activatableJSON is not None:
            actions.append(activatableJSON)
        
        return {'image':self.CHARACTER_IMAGES_DIRECTORY_URL+self.character.image,
                'actions':actions}