class Newton_Raphson:
    def __init__(self) -> None:
        self.F = []
        self.DF = []
        N = int(input("enter the number of variables : "))
        for i in range(0, N * 2, 2):
            power = int(input("Enter the power of x: "))
            constant = int(input(f"Enter the constant of power {power}: "))
            self.F.append(constant)
            self.F.append(power)
            if power != 0:
                constant *= power
                power -= 1
                self.DF.append(constant)
                self.DF.append(power)

    def f(self, x):
        value = 0
        for i in range(0, len(self.F), 2):
            value += self.F[i] * (x**self.F[i + 1])
        return value

    def df(self, x):
        value = 0
        for i in range(0, len(self.DF), 2):
            value += self.DF[i] * (x**self.DF[i + 1])
        return value

    def find_limit(self):
        if self.f(0) < 0:
            for i in range(100):
                if self.f(i) < 0 and self.f(i + 1) >= 0:
                    return i, i + 1

        else:
            for i in range(0, -100, 1):
                if self.f(i) >= 0 and self.f(i - 1) < 0:
                    return i + 1, i

    def solv(self, x0, E, itmax):
        root = 0
        ier = 1
        itnum = 1
        while itnum < itmax:
            denom = self.df(x0)

            if denom == 0:
                ier = 2
                break

            x1 = x0 - (self.f(x0) / denom)

            if abs(x1 - x0) < E:
                ier = 0
                root = x1
                break

            itnum += 1
            x0 = x1

        if ier == 0:
            print(f"the root of the equation is : {root}")
        elif ier == 1:
            print("max iteration reached")
        else:
            print("denominator is 0")


def main():
    obj = Newton_Raphson()
    l, u = obj.find_limit()
    x0 = (l + u) / 2
    obj.solv(x0, E=0.00005, itmax=10)


if __name__ == "__main__":
    main()
