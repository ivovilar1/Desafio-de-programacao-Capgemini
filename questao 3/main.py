
palavra = input('Digite a palavra:')  #variavel para pegar o valor do usuario
tamanho_palavra = len(palavra) #variavel para armazenar o tamanho da variavel palavra
contador_anagramas = 0 #variavel para armazenar a quantidade de anagramas encontrada


for i in range(tamanho_palavra): #um laço pra percorrer todo o tamanho da palavra
    for j in range(i+ 1, tamanho_palavra): #outro laço pra percorrer a partir da posição i+1
        substrings =''.join(sorted(palavra[i:j])) # a variavel substrings recebe as strings quebradas,o metodo join vai unir eles e o metodo sorted vai ordenar as informações
        tamanho_substrings = len(substrings) #variavel tamanho_subtrings recebe o tamanho das substrings

        for x in range(i+ 1, tamanho_palavra): #um laço pra percorrer a partir da posição i+1
            if x + tamanho_substrings > tamanho_palavra: #se o indice x somado ao tamanho da substring for maior que o tamanho_palavra, o laço é parado
                break
            substrings2 = ''.join(sorted(palavra[x:x+tamanho_substrings])) #a variavel subtrings2 recebe as strings quebradas, partindo da posição x até x + tamanho_substrings
            
            if substrings == substrings2: # se a substrings for igual a substrings2,o contador_anagramas será incrementado +1
                contador_anagramas +=1
print("A listagem de números pares de substrings é: {}".format(contador_anagramas))  #retornando para o usuario a contagem de anagramas

        
        