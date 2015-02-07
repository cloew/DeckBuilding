from Game.Zones.zone_types import CHARACTER
from Server.Game.Actions.activate_action_builder import ActivateActionBuilder
from Server.Json.character_wrapper import CharacterWrapper

class GameCharacterWrapper(CharacterWrapper):
    """ Wrapper to handle converting Game Characters to JSON """
    CHARACTER_IMAGES_DIRECTORY_URL = 'static/images/Characters/'
    
    def __init__(self, character, game):
        """ Initialize the Character Wrapper """
        self.game = game
        CharacterWrapper.__init__(self, character)
        
    def toJSON(self, playerId, includeActions=False):
        """ Return the card as a JSON Dictionary """
        actionBuilder = ActivateActionBuilder(CHARACTER, self.game, playerId)
            
        json = CharacterWrapper.toJSON(self)
        if includeActions and actionBuilder.canBuildFor(self.character):
            json['actions'] = [actionBuilder.buildFor(self.character)]
        return json