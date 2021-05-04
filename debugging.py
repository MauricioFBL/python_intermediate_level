def divisors(num):
    try:
        if num < 0:
            raise ValueError('no se deben usar numeros negativos')
        divisors = [i for i in range(1,num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return []

def run():
    try:
        num = int(input('Ingresaa un numero: '))
        print(divisors(num))
    except ValueError:
        print('Solo se pueden usar numeros')

if __name__ == '__main__': 
    run()