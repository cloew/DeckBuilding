
class InOperator:
    def compare(self, left, right):
        """ Compare the left and right hand sides """
        return left in right

operations = {"IN":InOperator()}