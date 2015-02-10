from Game.Characters.character_factory import CharacterFactory
from Server.helpers.json_factory import jsonFactory

from kao_flask.controllers.json_controller import JSONController

class GetCharactersController(JSONController):
    """ Controller to return all characters """
    
    def performWithJSON(self, json=None):
        characters = CharacterFactory.loadAll()
        return {'characters':jsonFactory.toJson([character for character in characters])}