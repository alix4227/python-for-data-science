
import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self):
        self.numbersOfBeverages = 0
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90
        def description(self):
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self, message):
            super().__init__(message)

    def repair(self):
        self.numbersOfBeverages = 0
        print("Coffee Machine repaired!")

    def serve(self, beverage):
        self.numbersOfBeverages += 1
        if (self.numbersOfBeverages > 10):
            raise(self.BrokenMachineException("This coffee machine has to be repaired."))
        if random.randint(0, 1):
            return beverage
        else:
            return self.EmptyCup()


def main():
    try:
        coffee = CoffeeMachine()
        for i in range(11):
            print(coffee.serve(Cappuccino()))
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
    try:
        coffee.repair()
        for i in range(11):
            print(coffee.serve(Coffee()))
    except CoffeeMachine.BrokenMachineException as e:
            print(e)


if __name__ == '__main__':
    main()