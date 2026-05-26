class HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.30):
        self.name = name
        self.price = price
    def description(self):
        return("Just some hot water in a cup.")
    def __str__(self):
        return(f"-----------------\n"
            f"name : {self.name}\n"
                f"price : {self.price:.2f}\n"
                f"description : {self.description()}")
    
class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return("Un po’ di Italia nella sua tazza!")


def main():
    bev = HotBeverage()
    print(bev)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    choco = Chocolate()
    print(choco)
    cappuccino = Cappuccino()
    print(cappuccino)

if __name__ == '__main__':
    main()