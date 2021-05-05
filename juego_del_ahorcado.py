import random
import os

def read():
    words = []
    with open('archivos/data.txt', 'r', encoding = 'utf-8') as f:
        for line in f:
            words.append(line)
    return words

def count_lines():
    data = read()
    data = {i:word for i,word in enumerate(data)}
    word_index = random.randint(0, len(data))
    word = data[word_index].replace('\n','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').lower()
    respond = ('_' * (len(data[word_index]) - 1))
    errors = 0
    while respond != word and errors < 10:
        try:
            letter = (input('ingresa una letra: \n'+ respond +'\n' )).replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').lower()
            assert len(letter)== 1,'cadena muy larga'
            respond = list(respond)
            if word.find(letter) != -1:
                indices = [l for l in range(len(word)) if word[l] == letter]
                for l in range(len(word)):
                    if l in indices:
                        respond[l] = letter
            else:
                errors += 1
            respond = "".join(respond)
            os.system('cls')
            print(' _____________')
            print('| ERRORES: ', errors,'|')
            print('|_____________|\n')
        except AssertionError:
            print('Solo se puede ingresar un caracter')
    if errors < 6:
        print('Felicidades, ganasete!!!! la palabra era: ',respond)
    else:        
        print('Se acabaron los intentos, PERDISTE!! la palabra era: ',word)

def run():
    print('             JUEGO DEL AHORCADO')
    jugar = '1'
    while jugar == '1':
        count_lines()
        print('\n\nPARA VOLVER A JUGAR PRESIONE EL NUMERO: "1" ')
        print('PARA SALIR PRESIONE CUALQUIER OTRA TECLA ')
        jugar = input('')

if __name__ == '__main__':
    run()