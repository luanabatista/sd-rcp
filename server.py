from Pyro5.api import expose, behavior
from counter import Counter
import Pyro5.api

# Marca a classe (ou método) que vai ser exposta em chamadas remotas
@expose

# Especifica o comportamento do server
# Neste caso, uma única instância será criada e usada para para todas as chamadas de método ("single")
@behavior(instance_mode="single")
class CounterServer(object):

    def __init__(self):
        # Array que armazena todos os contadores criados
        self.content = []

    # Cria um novo contador a partir do nome e valor fornecidos pelo usuario
    # Após a criação do contador retorna uma mensagem que indica sua criação 
    def createCounter(self, name, value):
        # Se o array content estiver vario, cria um novo contador
        if self.content == []:
            self.content.append(Counter(name, value))  
            return f"\n{name} de valor {value} criado."
        
        # Caso o array não esteja vazio, verifica se já existe um contador de mesmo nome
        # Se existir uma mensagem de erro é retornada 
        # Se não, então um novo contador é criado
        else:
            for c in self.content:
                if c.name == name:
                    return '\nJá existe um contador com este nome.'
                else:
                    self.content.append(Counter(name, value))  
                    return f"\n{name} de valor {value} criado." 
    
    # Incrementa um contador a partir de seu nome
    def incrementCounter(self, name):
        for c in self.content:

            # Caso o nome seja válido, o contador é incremementado em 1 e nome e o valor atual do contador são retornados
            if c.name == name:
                c.value += 1
                return f"\n{c.name} incrementado, valor atual: {c.value}."

        # Caso o nome dado não esteja registrado é exibida uma mensagem de erro     
        return "\n[Erro]: não foi possível incrementar, este contador não existe."

    # Acessa um contador a partir de seu nome, retornando seu nome e valor atual 
    def getCounter(self, name):
        for c in self.content:
            if c.name == name:
                return f"\n{c.name}, valor atual: {c.value}."

        # Caso o nome dado não esteja registrado é exibida uma mensagem de erro
        return "\n[Erro]: não foi possível acessar, este contador não existe."

# Programa principal
# Cria um daemon
daemon = Pyro5.server.Daemon()

# Encontra o nome do servior
ns = Pyro5.api.locate_ns()

# Registra o CounterServer como um objeto pyro
uri = daemon.register(CounterServer)

# Registra o objeto com um nome no servidor
ns.register("counterserver", uri)

print("Ready.")
daemon.requestLoop()   