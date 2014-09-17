from character import Character

from Game.Effects.Activatables.activatable_factory import ActivatableFactory
from Game.Effects.Triggers.trigger_factory import TriggerFactory

import resources.resource_manager as resource_manager

import json

class CharacterFactory:
    """ Factory to construct characters """
    CHARACTER_FILENAME = resource_manager.GetResourcePath("characters.json")
    
    def __init__(self):
        """ Initialize the Character Factory """
        self.__charactersJSON__ = None
        
    def loadCharacter(self, characterName):
        """ Load the card with the given name """
        characterJSON = self.findCharacterJson(characterName)
        if characterJSON is not None:
            name = characterJSON["name"]
            image = None
            if "image" in characterJSON:
                image = characterJSON["image"]
            return Character(name, triggers=self.loadTriggers(characterJSON), activatable=self.loadActivatable(characterJSON), image=image)
        else:
            print "Unable to load Character:", characterName
        return None
        
    def findCharacterJson(self, characterName):
        """ Find the proper character JSON """
        matchingCharactersJson = [characterJSON for characterJSON in self.cardsJson if characterJSON["name"] == characterName]
        if len(matchingCharactersJson) > 0:
            return matchingCharactersJson[0]
        return None
        
    def loadTriggers(self, characterJSON):
        """ Load the Character's Trigger Effects """
        triggers = []
        if "triggers" in characterJSON:
            triggers = TriggerFactory.loadTriggers(characterJSON["triggers"])
        return triggers
        
    def loadActivatable(self, characterJSON):
        """ Load the Character's Activatble Effect, if any """
        activatableEffect = None
        if "activatableEffect" in characterJSON:
            activatableEffect = ActivatableFactory.loadActivatable(characterJSON["activatableEffect"])
        return activatableEffect
            
    @property
    def cardsJson(self):
        """ Lazy-load the card Json """
        if self.__charactersJSON__ is None:
            self.loadJson()
        return self.__charactersJSON__
        
    def loadJson(self):
        """ Load the Character JSON """
        with open(self.CHARACTER_FILENAME, 'r') as file:
            self.__charactersJSON__ = json.load(file)
            
            
CharacterFactory = CharacterFactory()