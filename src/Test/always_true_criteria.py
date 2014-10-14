
class AlwaysTrueCriteria:
    """ A Criteria that always returns true """
    
    def compare(self, card, context):
        """ Compare the card with the context """
        return True