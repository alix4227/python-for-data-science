class calculator:
    def __init__(self, list):
        self.list = list

    def __add__(self, object) -> None:
        for i in range(len(self.list)):
            self.list[i] += object
        print(self.list)

    def __mul__(self, object) -> None:
        for i in range(len(self.list)):
            self.list[i] *= object
        print(self.list)

    def __sub__(self, object) -> None:
        for i in range(len(self.list)):
            self.list[i] -= object
        print(self.list)

    def __truediv__(self, object) -> None:
        if (object == 0):
            print("Error: division by 0")
            return
        for i in range(len(self.list)):
            self.list[i] /= object
        print(self.list)