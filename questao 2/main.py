senha = input('Digite sua senha segura:') #variavel senha para armazenar o valor da senha

senha_ideal = 'aaaaaa' #o intuito dessa variavel é o seguinte: como o tamanho da senha é fixo(6), eu criei essa variavel com um tamanho fixo para comparar ela com a variavel senha

if len(senha) == len(senha_ideal): #um if para verificar se o tamanho da senha é igual ao tamanho da senha_ideal
    print('senha segura!')            #sendo verdadeiro, a senha está ok
elif len(senha) < len(senha_ideal): # se o tamanho da senha for menor que a senha_ideal cairá na outra condição
    diferenca = len(senha_ideal) - len(senha) #variavel diferença vai receber a diferença do tamanho da senha_ideal e o tamanho da senha
    print("Para sua senha ficar segura, adicione mais {} caracteres".format(diferenca))
