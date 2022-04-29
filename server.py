from Pyro5.api import expose, behavior
from counter import Counter
import Pyro5.api

# Marca a classe (ou método) que vai ser exposta em chamadas remotas
@expose

# Especifica o comportamento do server
# Uma única instância será criada e usada para para todas as chamadas de método ("single")
@behavior(instance_mode="single")
class CounterServer(object):

    def __init__(self):
        self.content = []

    # Recebe e printa nome e valor do contador criado
    def createCounter(self, name, value):
        if self.content == []:
            self.content.append(Counter(name, value))  
            return f"\n{name} de valor {value} criado."
        
        # Caso já exista um contador com o mesmo nome, é exibida uma mensagem
        # Pede novamente nome e valor para criar o contador
        else:
            for c in self.content:
                if c.name == name:
                    return '\nJá existe um contador com este nome.'
                else:
                    self.content.append(Counter(name, value))  
                    return f"\n{name} de valor {value} criado." 
    
    # Pede o nome do contador que o usuário deseja incrementar
    def incrementCounter(self, name):
        for c in self.content:

            # Caso o nome seja válido, o contador é incrmementado em 1 e nome e o valor atual do contador são exibidos
            if c.name == name:
                c.value += 1
                return f"\n{c.name} incrementado, valor atual: {c.value}."

        # Caso o nome dado não esteja registrado é exibida uma mensagem        
        return "\n[Erro]: não foi possível incrementar, este contador não existe."

    # Exibe o nome e o valor atual do contador
    def getCounter(self, name):
        for c in self.content:
            if c.name == name:
                return f"\n{c.name}, valor atual: {c.value}."

        # Caso o nome dado não esteja registrado é exibida uma mensagem
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