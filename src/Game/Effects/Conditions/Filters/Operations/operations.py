import operator

def inOperator(value, container):
    return operator.contains(container, value)
    
def compareEvenOrOdd(value, expected):
    return self.getEvenOrOdd(value) == expected
    
def getEvenOrOdd(self, value):
    options = {0:"EVEN", 1:"ODD"}
    return options[value % 2]

operations = {"==":operator.eq,
              ">=":operator.ge,
              "<=":operator.le,
              "IN":inOperator,
              "EVEN_OR_ODD":compareEvenOrOdd}