import sys


class Plant:
    def __init__(self, name, height, age):
        self.name: str = name
        self.height: int = height
        self.age: int = age
    def show(self):
        print(f'{self.name}: {self.height}cm, {self.age} days old')

def main(args):
    plant = Plant("Rose", 25, 30)
    plant.show()

if __name__ == "__main__":
    main(sys.argv)