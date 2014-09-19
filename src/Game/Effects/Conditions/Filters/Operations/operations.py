import operator

def inOperator(value, container):
    return operator.contains(container, value)

operations = {"==":operator.eq,
              ">=":operator.ge,
              "<=":operator.le,
              "IN":inOperator}