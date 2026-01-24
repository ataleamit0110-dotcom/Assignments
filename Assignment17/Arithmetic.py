def add(no1, no2):
    return no1 + no2

def sub(no1, no2):
    return no1 - no2

def mul(no1, no2):
    return no1 * no2

def div(no1, no2):
    if no2 != 0:
        return no1 / no2
    else:
        return "Division by zero is not allowed"
