class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


obj1 = Numbers(28)
#obj2 = Numbers(17)

print("Number:", obj1.Value)
print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())
