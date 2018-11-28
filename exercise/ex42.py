# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a object
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a object
class Employee(Person):

    def __init__(self, name, salary):
        # Implement the `.__init__` method
        # from the superclass of `Employee
        # (i.e. Person.__init__(name))
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# mary has-a pet has-a name: satan
mary.pet = satan

# Frank is-a Employee has-a salary: 120000
frank = Employee("Frank", 120000)

# Frank has-a Dog has-a name: Rover
frank.pet = rover

# Flipper is-a Fish
flipper = Fish()

# Crouse is-a Salmon and Fish
crouse = Salmon()

# Harry is-a Halibut and fish
harry = Halibut()
