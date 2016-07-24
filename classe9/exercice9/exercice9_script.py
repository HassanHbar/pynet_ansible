#!/usr/bin/env python
"""
Write a Python script in a different directory (not the one containing mytest).

    a. Verify that you can import mytest and call the three functions func1(), func2(), and func3(). 
    b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
"""
from mytest import func1, func2, func3, MyClass

def main():
    print " function 1 display: \n"
    func1()
    print "\n"
    print " function 2 display: \n"
    func2()
    print "\n"
    print " function 3 display: \n"
    func3()
    print "\n"
    print " MyClass  display: \n"
    my_obj = MyClass( "January", 2, "Mach")
    my_obj.x
    print "\n"
    my_obj.y
    print "\n"
    my_obj.z
    print "\n"
    my_obj.hello()
    print "\n"
    my_obj.not_hello()
    print "\n"
if __name__ == "__main__":
    main()
