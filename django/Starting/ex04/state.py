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
    for state, capital in capital_cities.items():
        if capital == args[1]:
            for key, value in states.items():
                if state == value:
                    print(f'{key}')
                    return 1
    print('Unknown capital city')
if __name__ == '__main__':
    capital_city(sys.argv)