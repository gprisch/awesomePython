class Mammal:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def speak(self):
        print('my name is ', self.name)

    def call_out(self):
        """ polymorphism """
        self.speak()


class Cat(Mammal):
    def speak(self):
        print('Miaouuu')


class Dog(Mammal):
    def __init__(self, name, size, breed):
        super().__init__(name, size)
        self.breed = breed

    def speak(self):
        print('Wouf wouf')


if __name__ == '__main__':
    mam = Mammal('Ted', 1.8)
    felix = Cat('Felix', .4)
    fido = Dog('Fido', .6, 'Labrador')

    mam.call_out()
    felix.call_out()
    fido.call_out()
