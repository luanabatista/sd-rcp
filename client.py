from Pyro5.api import Proxy

# Cria proxy do Pyro para objetos remotos
# Intercepta chamadas de metodos e as envia para o objeto remoto
counterserver = Proxy("PYRONAME:counterserver")

# Cria um loop que fica recebendo valores do usuário
while True:

    # Cria menu que apresenta as ações que o usuário pode executar
    menu = int(input("\nMENU\n1) Criar contador\n2) Acessar contador\n3) Incrementar contador\n4) Finalizar\n\nSelecione uma opção: "))
    if menu == 1:
        name = input("Digite o nome do contador: ")
        value = int(input("Digite o valor inicial do contador: "))

        # Estabelece a condição que o valor inicial do contador deve ser um número inteiro
        if (type(value) is int):
            print(counterserver.createCounter(name, value))
        
        # Caso não seja exibe uma mensagem de erro
        else:
            print('[Erro]: não foi possível criar, o valor inserido deve ser um número inteiro.')
    
    # Exibe o valor de um determinado contador a partir de seu nome 
    elif menu == 2:
        name = input("Digite o nome do contador a ser acessado: ")
        print(counterserver.getCounter(name))

    # Incrementa o contador e exibe o seu valor após ser incrementado
    elif menu == 3:
        name = input("Digite o nome do contador a ser incrementado: ")
        print(counterserver.incrementCounter(name))

    # Finaliza o programa
    elif menu == 4:
        exit(0)

    # Qualquer valor fora que não esteja entre 1 e 4 finaliza o programa
    else:
        exit(0)