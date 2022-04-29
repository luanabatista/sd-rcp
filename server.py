from Pyro5.api import expose, behavior
from counter import Counter
import Pyro5.api

@expose
@behavior(instance_mode="single")
class CounterServer(object):

    def __init__(self):
        self.content = []

    def createCounter(self, name, value):
        if self.content == []:
            self.content.append(Counter(name, value))  
            return f"\n{name} de valor {value} criado."
        else:
            for c in self.content:
                if c.name == name:
                    return '\nJá existe um contador com este nome.'
                else:
                    self.content.append(Counter(name, value))  
                    return f"\n{name} de valor {value} criado." 
        
    def incrementCounter(self, name):
        for c in self.content:
            if c.name == name:
                c.value += 1
                return f"\n{c.name} incrementado, valor atual: {c.value}."
                
        return "\n[Erro]: não foi possível incrementar, este contador não existe."

    def getCounter(self, name):
        for c in self.content:
            if c.name == name:
                return f"\n{c.name}, valor atual: {c.value}." 
                
        return "\n[Erro]: não foi possível acessar, este contador não existe."

# main program
daemon = Pyro5.server.Daemon()         # make a Pyro daemon
ns = Pyro5.api.locate_ns()             # find the name server
uri = daemon.register(CounterServer)   # register the CounterServer as a Pyro object
ns.register("counterserver", uri)      # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()   