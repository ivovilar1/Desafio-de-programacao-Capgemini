
print('''
******************

Escada em Python

******************
''')
try:    #um try só pra evitar que o programa quebre de cara
    
    n = int(input('Informe o valor de n: ')) #variavel pra armazenar o valor da escada de *


    for n_linhas in range(n):   #um for pra varrer a quantidade de linhas em n
        espacos = n - n_linhas -1   #variavel espaço pra calcular os espaços dos * 
        asteriscos =1 + n_linhas    #variavel asteriscos para calcular a quantidade de *
        print(" "*espacos+"*"*asteriscos)    #um print para mostrar a escada de *
except:
    print('Por favor, entre com um valor inteiro')