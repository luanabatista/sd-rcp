from Pyro5.api import Proxy

counterserver = Proxy("PYRONAME:counterserver")

while True:
    menu = int(input("\nMENU\n1) Criar contador\n2) Acessar contador\n3) Incrementar contador\n4) Finalizar\n\nSelecione uma opção: "))
    if menu == 1:
        name = input("Digite o nome do contador: ")
        value = int(input("Digite o valor inicial do contador: "))
        if (type(value) is int):
            print(counterserver.createCounter(name, value))
        else:
            print('[Erro]: não foi possível criar, o valor inserido deve ser um número inteiro.')
    
    elif menu == 2:
        name = input("Digite o nome do contador a ser acessado: ")
        print(counterserver.getCounter(name))

    elif menu == 3:
        name = input("Digite o nome do contador a ser incrementado: ")
        print(counterserver.incrementCounter(name))

    elif menu == 4:
        exit(0)

    else:
        exit(0)