import operator

def inOperator(value, container):
    return operator.contains(container, value)

operations = {">=":operator.__ge__,
              "<=":operator.__le__,
              "IN":inOperator}