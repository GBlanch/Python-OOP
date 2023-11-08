work in progress

python ```#!/usr/bin/env python
#coding: utf-8#

#Instance, Class and Static Methods#

class class_example:
    def instance_m(self):
        return 'instance method called', self
    
    def class_m(cls):
        return 'class method called', cls

    def static_m():
        return 'static method called'


# In[168]:


print("1st method is: {},\n\n2nd one is:{}\n\nand the last one is:{}".format(obj.instance_m(),
obj.class_m(),obj.static_m))


# Solely showing the type of the method:

# In[55]:


class Sample():
    pass

x = Sample()
type(x)


#Short self-intro class, with merely 2 arguments#

class intro():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def hello(self):
        print("Salut")
        
    def report(self):
        print("Je m'appelle {} {}".format(self.first_name, self.last_name))

i = intro('Gerry', 'Blanch')
i.hello()
i.report()

class Agent():
    country = 'SPA'
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print('Hi Agent {} and from {}'.format(self.name, country))

obj = Agent('Gerry')

obj = class_example()
obj.method()


#Methods#

import math

pi = math.pi

class circle_properties():

    def __init__(self, radius):
        self.rad = radius
        
    def permieter(self):
        return 2 * pi * self.rad
    
    def area(self):
        return pi * self.rad ** 2 

circle_1 = circle_properties(3)
circle_1.rad

circle_1.permieter()

circle_1.area()

class rectangle_properties(): 
    def __init__(self,le = 0,wi = 0): 
        self.lenght = le
        self.width = wi 
    def area (self): 
        """Find the area of rectangle""" 
        return (self.lenght * self.width) 

rect_1 = rectangle_properties(1.3,5) 
print ("The area of the rectangle is", rect_1.area(),"sqft.")


#Special Methods#

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f'''
The title is {self.title}, the author is {self.author} and it has {self.pages} pages'''


b = Book('"The Chimp Paradox"', 'Steve Peters', 372)
print(b)
```
