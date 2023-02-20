class Calc:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

    def result(self):
        resultant1 = calc.add(2, 3)
        resultant2 = calc.multiply(4, 5)
        resultant3 = calc.subtract(3, 2)
        resultant4 = calc.divide(2, 3)
        outputting = f"""the result of a and b is = {resultant1}, the result of 4 * 5 = {resultant2}, the result of subtracting 2 from 3 is {resultant3} 
    and the result of dividing 2 / 3 is {resultant4}"""
        return outputting


calc = Calc()
