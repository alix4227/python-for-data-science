import sys

def capital_city(args):
    if len(args) != 2:
        return 0
    states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
    capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}
    for key, value in states.items():
        if key == args[1]:
            for state, capital in capital_cities.items():
                if state == value:
                    print(f'{capital}')
                    return 1
    print('Unknown state')
if __name__ == '__main__':
    capital_city(sys.argv)