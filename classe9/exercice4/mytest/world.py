#!/usr/bin/env python 
"""week 9, exercice 4"""
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

if __name__ == "__main__":
    print "the module  world.py do some thing"
