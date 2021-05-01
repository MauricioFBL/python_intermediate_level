# list comprehensions
def run():
    squares = []
    for i in range(1,101):
        squares.append(i**2)

    print("Cuadrados del 1 al 100: \n",squares)
    three_multiples = []
    for i in range(1,101):
        if i % 3 != 0:
            three_multiples.append(i**3)

    print("\nCuadrados de los no multiplos de 3: \n",three_multiples)
    # List comprehension
    # SINTAXIS
    # [element for element in iterable if condition]
    # Donde:
    # element: elemento a colocar en la listas
    # for element in iterable: del que se extrtaen elementos
    # if condition: condicion a cumplir
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    my_list = [i for i in range(1,100000) if i % 36 == 0 ]
    print("\nreto: \n",my_list)


if __name__ == '__main__':
    run()