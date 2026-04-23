import sys

class Plant:
    
    def __init__(self, name: str, height: float, age: int, growth: float):
        if height < 0 or age < 0 or growth < 0:
            raise ValueError("value error")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Not a string")
        self.__name: str = name
        self.__height: float = height
        self.__age_days: int = age
        self.__total_growth: float = 0
        self.__growth: float = growth
    
    def show(self):
        print('=== Garden Plant Growth ===')
        print(f'{self.__name}: {round(self.__height, 2)}cm, {self.__age_days} days old')
        for i in range(1, 8):
            self.grow(self.__growth)
            self.__total_growth += self.__growth
            self.age(1)
            self.showGrowth(i)
        print(f'Growth this week: {self.__total_growth}cm')
    
    def showGrowth(self, day):
        print(f'=== Day {day} ===')
        print(f'{self.__name}: {round(self.__height, 2)}cm, {self.__age_days} days old')
    
    def grow(self, i: float):
        self.__height += i

    def age(self, i: int):
        self.__age_days += i
        


def main(args):
    try:
        rose = Plant("Rose", 25, 30, 0.8)
        rose.show()
        rose.__name = "Lechat"
        rose.show()
    except ValueError as e:
        print(f'{e}')
    

if __name__ == "__main__":
    main(sys.argv)