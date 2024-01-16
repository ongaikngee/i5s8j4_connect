class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Woof woof')


my_dog = Dog('Lucky', 10)
my_dog.bark()
