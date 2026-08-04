import sys

def is_state(item, states, capital_cities):
    for state, city_initials in states.items():
        if item.strip().upper() == state.upper():
            for initial, capital in capital_cities.items():
                if initial == city_initials:
                    print(f'{capital} is the capital of {state}')
                    return 1
    return 0

def is_capital_city(item, states, capital_cities):
    for initial, capital in capital_cities.items():
        if item.strip().upper() == capital.upper():
            for state, city_initials in states.items():
                if city_initials == initial:
                    print(f'{capital} is the capital of {state}')
                    return 1
    return 0

def main(args):
    if len(args) != 2:
        return 0
    arguments = args[1].split(",")
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
    for item in arguments:
        if not item.strip():
            continue
        if is_state(item,states,capital_cities):
            continue
        elif is_capital_city(item,states,capital_cities):
            continue
        else:
            print(f'{item.strip()} is neither a capital city nor a state')
        
if __name__ == '__main__':
    main(sys.argv)