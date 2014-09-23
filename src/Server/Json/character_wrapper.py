
class CharacterWrapper:
    """ Wrapper to handle converting Characters to JSON """
    CHARACTER_IMAGES_DIRECTORY_URL = 'static/images/Characters/'
    
    def __init__(self, character):
        """ Initialize the Character Wrapper """
        self.character = character
        
    def toJSON(self):
        """ Return the card as a JSON Dictionary """
        return {'image':self.CHARACTER_IMAGES_DIRECTORY_URL+self.character.image,
                'name':self.character.name}