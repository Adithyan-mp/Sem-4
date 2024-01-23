
class KnapSack:
    def __init__(self):
        self.weight = []
        self.value = []
        self.capacity = 0
        self.count = 0

    def get_data(self):
        print("ENTER HOW MANY ITEMS ARE THERE: ", end="")
        self.count = int(input())
        self.weight = [0] * (self.count + 1)
        self.value = [0] * (self.count + 1)

        # Initialize the first element to 0 for both weight and value
        self.weight[0] = 0
        self.value[0] = 0

        print("Enter weight and value of the items respectively:")
        for i in range(1, self.count + 1):
            self.weight[i] = int(input(f"Weight ({i}): "))
            self.value[i] = int(input(f"Value ({i}): "))

        print("Enter maximum capacity: ", end="")
        self.capacity = int(input())
        input()  # Clear the input buffer

    def get_weight(self, i):
        return self.weight[i]

    def get_value(self, i):
        return self.value[i]

    def get_capacity(self):
        return self.capacity

    def get_count(self):
        return self.count

    def get_max_item(self):
        minisack = [[0] * (self.capacity + 1) for _ in range(self.count + 1)]

        for i in range(1, self.count + 1):
            for j in range(self.capacity + 1):
                if j - self.weight[i] < 0:
                    minisack[i][j] = minisack[i - 1][j]
                else:
                    minisack[i][j] = max(minisack[i - 1][j], self.value[i] + minisack[i - 1][j - self.weight[i]])

        self.trace_back(minisack)

        return minisack[self.count][self.capacity]

    def trace_back(self, sack):
        i = self.count
        j = self.capacity
        while i > 0 and j > 0:
            if j - self.weight[i] >= 0 and sack[i][j] == self.value[i] + sack[i - 1][j - self.weight[i]]:
                # Item i is included in the optimal solution
                print(f"Item {i}: Weight = {self.weight[i]}, Value = {self.value[i]}")
                j -= self.weight[i]
            i -= 1


def main():
    sack = KnapSack()
    sack.get_data()
    max_item_value = sack.get_max_item()
    print(f"Maximum value for the knapsack: {max_item_value}")


if __name__ == "__main__":
    main()
                  