# dict comprehensions
def run():
    my_dict = {}

    for i in range(1,101):
        my_dict[i] = i**3

    my_dict = {}
    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i ** 3
    
    # DICT comprehension
    # SINTAXIS
    # [key:value for key in iterable if condition]
    # Donde:
    # element: elemento a colocar en la listas
    # for element in iterable: del que se extrtaen elementos
    # if condition: condicion a cumplir
    my_dict = {i:i**3 for i in range(1,101) if i % 3 != 0}    
    # print(my_dict)

    my_dict = {x:x**(1/2) for x in range(1,1001)}
    print(my_dict)

if __name__ == '__main__':
    run()