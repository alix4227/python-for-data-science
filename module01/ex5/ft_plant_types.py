import sys

class Plant:
    
    def __init__(self, name: str, height: float, age: int, growth: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Not a string")
        if not isinstance(height, float):
            raise ValueError("Not a float")
        if not isinstance(age, int):
            raise ValueError("Not an int")
        if height < 0 or age < 0 or growth < 0:
            raise ValueError("value error")
        self._name: str = name
        self._height: float = height
        self._age_days: int = age
        self._total_growth: float = 0
        self._growth: float = growth
    
    def showPlant(self):
        print('=== Garden Plant Growth ===')
        print(f'{self._name}: {round(self._height, 2)}cm, {self._age_days} days old')
        for i in range(1, 8):
            self.grow(self._growth)
            self._total_growth += self._growth
            self.age(1)
            self.showGrowth(i)
        print(f'Growth this week: {self._total_growth}cm')
    
    def show(self):
        print('=== Garden Plant Growth ===')
        print(f'{self._name}: {round(self._height, 2)}cm, {self._age_days} days old')

    def showGrowth(self, day):
        print(f'=== Day {day} ===')
        print(f'{self._name}: {round(self._height, 2)}cm, {self._age_days} days old')
    
    def grow(self, i: float):
        self._height += i

    def age(self, i: int):
        self._age_days += i

    def get_height(self)->float:
        return (self._height)
    
    def get_age(self)->int:
        return (self._age_days)
    
    def set_age(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Wrong type: value is not an integer")
        if value < 0:
            raise ValueError("age value error")
        self._age_days = value

    def set_height(self, value):
        if not isinstance(value, float):
            raise ValueError("Wrong type: value is not a float")
        if value < 0:
            raise ValueError("height value error")
        self._height = value
        
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth: float, color: str):
        super().__init__(name, height, age, growth)
        if not isinstance(color, str):
            raise ValueError("Not a string")
        self._color = color
    def bloom(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Not a boolean")
        blooming = value
        if blooming:
            print(f' {self._name} is blooming beautifully!')
        else:
            print(f'{self._name} has not bloomed yet')
    def show(self):
        print('=== Flower')
        print(f'{self._name}: {round(self._height, 2)}cm, {self._age_days} days old')
        print(f' Color: {self._color}')


def main(args):
    try:
        rose= Plant("Rose", 25.0, 30, 0.8, "red")
        rose = Flower()
        rose.age(2)
        rose.show()
        rose.bloom(True)
    except ValueError as e:
        print(f'{e}')
    

if __name__ == "__main__":
    main(sys.argv)