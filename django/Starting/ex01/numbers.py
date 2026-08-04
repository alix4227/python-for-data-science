def my_split():
    with open('numbers.txt', 'r') as file:
        lines = file.read().split(',')
        for line in lines:
            number = int(line)
            print(f'{number}')

if __name__ == '__main__':
    my_split()