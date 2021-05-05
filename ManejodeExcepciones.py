# Excepciones
# Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.
# TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
# EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
# ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
# FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.
def palindrome(word):
    try:
        if len(word) == 0:
            raise ValueError('no se pueden usar cadenas vacias')
        return word == word[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(palindrome(''))
    except TypeError:
        print('Solo puedes usar cadenas de texto')

if __name__ == '__main__':
    run()