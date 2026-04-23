import sys

class Plant:
    
    def __init__(self, name: str, height: float, age: int, growth: float):
        self.name: str = name
        if height < 0 or age < 0 or growth < 0:
            raise ValueError("value error")
        if not isinstance(name, str):
            raise ValueError("Not a string")
        self.height: float = height
        self.age_days: int = age
        self.total_growth: float = 0
        self.growth: float = growth
    
    def show(self):
        print('=== Garden Plant Growth ===')
        print(f'{self.name}: {round(self.height, 2)}cm, {self.age_days} days old')
        for i in range(1, 8):
            self.grow(self.growth)
            self.total_growth += self.growth
            self.age(1)
            self.showGrowth(i)
        print(f'Growth this week: {self.total_growth}cm')
    
    def showGrowth(self, day):
        print(f'=== Day {day} ===')
        print(f'{self.name}: {round(self.height, 2)}cm, {self.age_days} days old')
    
    def grow(self, i: float):
        self.height += i

    def age(self, i: int):
        self.age_days += i
        


def main(args):
    try:
        rose = Plant(15, 25, 30, 0.8)
        rose.show()
    except ValueError as e:
        print(f'{e}')
    

if __name__ == "__main__":
    main(sys.argv)