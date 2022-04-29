from Pyro5.api import expose

# Marca a classe (ou método) que vai ser exposta em chamadas remotas
@expose
# Classe do contador
class Counter(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value