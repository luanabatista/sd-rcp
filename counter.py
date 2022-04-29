from Pyro5.api import expose

@expose
class Counter(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value