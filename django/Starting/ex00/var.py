
def my_var():
    nombre:int = 42
    string:str = '42'
    string2:str = 'quarante-deux'
    flow:float = 42.0
    boobool:bool = True
    lists:list = [42]
    dictio:dict = {42:42}
    tuples:tuple = (42,)
    sets:set = set()
    table = [nombre, string, string2, flow, boobool, lists, dictio, tuples, sets]
    for i in table:
        print(f'{i} est de type {type(i)}')

if __name__ == '__main__':
    my_var()