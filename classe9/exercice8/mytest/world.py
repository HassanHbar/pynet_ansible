#!/usr/bin/env python 
"""week 9, exercice 8"""
def func1():
    print "Hello World"

class MyClass(object):
    """Create a class MyClass that require that three variables be passed in upon initialization. """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        print "Hello World: {} {} {}".format(self.x, self.y, self.z)

    def not_hello(self):
        print "NOT Hello World: {} {} {}".format(self.x, self.y, self.z)

class MyChildClass(MyClass):

    """ the child class should do something additional in the __init__() method yet 
    still call its parent class __init__()."""

    def __init__(self, x1, x2, x3):
        print "doing something additional in the __init__() method"
        MyClass.__init__(self, x1, x2, x3)

    """" Write a child class MyChildClass of MyClass. This child class should 
    override the 'hello' method and print a different statement"""

    def hello(self):
        print "This Class overide Hello orld Class: {} {} {}".format(self.x, self.y, self.z)

if __name__ == "__main__":
    print "the module  world.py do some thing"
