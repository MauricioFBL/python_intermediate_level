# High order functions
# son funciones que reciben como prametro a otra funcion
# Existen 3 principales:jilter, map, reduce
from functools import reduce

def run():
    my_list = [1,4,5,6,9,13,19,21]
    odd = [i for i in my_list if i % 2 != 0]
    print(odd)
    # Filter: filtra los valores de una lista
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd)
    my_list = [1,2,3,4,5]
    squared = [i**2 for i in my_list]
    print(squared)    
    # map: aplica trnsformacion de valores
    squared = list(map(lambda x: x**2, my_list))
    print(squared)
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print(all_multiplied)

# La diferencia entre filter y map:d
#     filter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
#     Map funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.
# Cómo funciona reduce:
#     Reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

if __name__ == '__main__':
    run()