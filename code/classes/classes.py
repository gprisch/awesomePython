# a class to be implemented later
# class Car:
#     pass


class Car:
    # acceleration: float = 3.0
    # mpg: int = 25

    def __init__(self, acceleration, mpg):
        self.acceleration = acceleration
        self.mpg = mpg
        self.__color = 'red'  # private

    def print_info(self):
        print('Acceleration: %.2f \nmpg: %d' % (self.acceleration, self.mpg))


if __name__ == '__main__':
    car = Car(4.0, 50)

    print('Acceleration: %.2f \nmpg: %d' % (car.acceleration, car.mpg))
    car.acceleration = 5.0
    print('Acceleration: %.2f \nmpg: %d' % (car.acceleration, car.mpg))
    # attribute added
    car.brand = 'Peugeot'
    print('Brand:', car.brand)
    car.print_info()
    # print('{}', car.__color)  # error
    
