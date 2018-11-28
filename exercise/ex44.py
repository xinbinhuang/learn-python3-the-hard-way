# Three ways that inheritance work
# 1. Actions on the child `imply` an action on the parent.
# 2. Actions on the child `override` the action on the parent.
# 3. Actions on the child `alter` the action on the parent.


class Parent(object):

    def override(self):
        print("PARENT overried()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


print("-----------INHERITANCE-----------")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super().altered()
        super(Child, self).altered()
        print("CILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

print('======Implicit======')
dad.implicit()
son.implicit()

print('======Override======')
dad.override()
son.override()

print('======Altered======')
dad.altered()
son.altered()


print("-----------COMPOSITION-----------")


class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered())")


son = Child()
print('======Implicit======')
son.implicit()
print('======Override======')
son.override()
print('======Altered======')
son.altered()
