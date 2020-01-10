class Rabbit(object):
     
    def __init__(self, name):
        self._name = name
     
    @staticmethod
    def newRabbit(name):
        return Rabbit(name)
     
    @classmethod
    def newRabbit2(cls):
        return Rabbit('')
     
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

rabbit = Rabbit('Tutu')
print(rabbit.name)
rabbit.name = "Dashe"
print(rabbit.name)