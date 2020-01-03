# it is not because you do something that you must do it
class Mammal:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def speak(self):
        print('my name is ', self.name)

    def call_out(self):
        """ polymorphism """
        self.speak()


class Pet:
    def __init__(self, nickname):
        self.nickname = nickname


class Cat(Mammal, Pet):
    def __init__(self, name, size, nick, breed):
        Mammal.__init__(self, name, size)
        Pet.__init__(self, nick)
        self.breed = breed

    def speak(self):
        print('Miaouuu')

    def to_string(self):
        print('%s aka. %s is a %s and is %.2f long' % (self.name,
                                                       self.nickname,
                                                       self.breed,
                                                       self.size))


if __name__ == '__main__':
    my_cat = Cat('Goliath', .4, 'Gogo', 'Maine coon')
    my_cat.speak()
    my_cat.to_string()
