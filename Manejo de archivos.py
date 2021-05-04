# Manejo de archivos
# Existen varias extensiones de archivos con los que podemos interactuar con python (js,csv,py,css,json,xml)
# Para abrir un archivo seguimos las siguiente estructura
# with open(<ruta>, <modo_apertura>) as <nombre>
# with Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)
# open(ruta,modo_apertura): es una función que necesita de dos parámetros
#     ruta: es donde se encuentra nuestro archivo en nuestro equipo
#     modo_de_apertura: como vamos a abrir el archivo, los modificadores son:
#     r → modo de lectura
#     w → modo de escritura (sobreescribe el archivo)
#     a → modo append (añade información al final del archivo)
# as <nombre> nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer
def run():
    pass

if __name__ == '__main__':
    run()