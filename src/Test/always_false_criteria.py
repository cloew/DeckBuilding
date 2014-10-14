
class AlwaysFalseCriteria:
    """ A Criteria that always returns false """
    
    def compare(self, card, context):
        """ Compare the card with the context """
        return False