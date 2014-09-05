import os

def GetResourcePath(resourceFilename):
    """ Returns the path to Resource directory """
    return os.path.join(GetResourceDirectory(), resourceFilename)
    
def GetResourceDirectory():
    """ Returns the path to Resource directory """
    return os.path.dirname(__file__)