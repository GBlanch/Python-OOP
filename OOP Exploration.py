#!/usr/bin/env python
# coding: utf-8

# ### Instance, Class and Static Methods

# In[145]:


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


# Short self-intro class, with merely 2 arguments:

# In[120]:


class intro():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def hello(self):
        print("Salut")
        
    def report(self):
        print("Je m'appelle {} {}".format(self.first_name, self.last_name))


# In[128]:


i = intro('Gerry', 'Blanch')
i.hello()
i.report()


# In[88]:


class Agent():
    country = 'SPA'
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print('Hi Agent {} and from {}'.format(self.name, country))

obj = Agent('Gerry')


# In[135]:


obj = class_example()
obj.method()


# ### Methods
# 

# In[52]:


import math

pi = math.pi


# In[93]:


class circle_properties():

    def __init__(self, radius):
        self.rad = radius
        
    def permieter(self):
        return 2 * pi * self.rad
    
    def area(self):
        return pi * self.rad ** 2 
    


# In[94]:


circle_1 = circle_properties(3)
circle_1.rad


# In[95]:


circle_1.permieter()


# In[96]:


circle_1.area()


# In[ ]:





# In[115]:


class rectangle_properties(): 
    def __init__(self,le = 0,wi = 0): 
        self.lenght = le
        self.width = wi 
    def area (self): 
        """Find the area of rectangle""" 
        return (self.lenght * self.width) 


# In[116]:


rect_1 = rectangle_properties(1.3,5) 
print ("The area of the rectangle is", rect_1.area(),"sqft.")


# ### Special Methods

# In[ ]:





# In[213]:


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


# In[215]:


b = Book('"The Chimp Paradox"', 'Steve Peters', 372)
print(b)

