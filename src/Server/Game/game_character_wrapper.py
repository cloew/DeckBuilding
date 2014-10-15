from json_helper import GetActivatableActionJSON
from Game.Sources.source_types import CHARACTER
from Server.Json.character_wrapper import CharacterWrapper

class GameCharacterWrapper(CharacterWrapper):
    """ Wrapper to handle converting Game Characters to JSON """
    CHARACTER_IMAGES_DIRECTORY_URL = 'static/images/Characters/'
    
    def __init__(self, character, game):
        """ Initialize the Character Wrapper """
        self.game = game
        CharacterWrapper.__init__(self, character)
        
    def toJSON(self, includeActions=False):
        """ Return the card as a JSON Dictionary """
        actions = []
        activatableJSON = GetActivatableActionJSON(self.character, self.game, source=CHARACTER)
        if activatableJSON is not None:
            actions.append(activatableJSON)
            
        json = CharacterWrapper.toJSON(self)
        if includeActions:
            json['actions'] = actions
        return json