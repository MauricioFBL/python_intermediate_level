# listas y diccionarios anidados
def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstnam": "Facundo", "lastname": "Garcia"}
    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Mauricio", "lastname": "Bautista"},
        {"firstname": "Fernado", "lastname": "Lopez"},
        {"firstname": "Susana", "lastname": "Garcia"},
        {"firstname": "Fernanda", "lastname": "Ramirez"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1.2,2.3,3.4,4.5,5.6]
    }

    for key, values in super_dict.items():
        print(key,": ", values)
    
    for element in super_list:
        for key, values in element.items():
            print(key,": ", values)

if __name__ == '__main__':
    run()