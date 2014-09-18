import operator

def inOperator(value, container):
    return operator.contains(container, value)

operations = {"<=":operator.__le__,
              "IN":inOperator}