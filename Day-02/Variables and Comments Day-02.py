#!/usr/bin/env python
# coding: utf-8

# In[1]:


#print syntax
print("Welcome to Python Programming")


# In[34]:


#Difference between printing with quotes and without quotes
programming_language = "Python"
print("programming_language")
print(programming_language)


# In[7]:


#printing desired variable
programming_language_1 = "Python"
programming_language_2 = "Java"
print(programming_language_2)


# In[9]:


#variable name shouldnot start with a number
2programming_language = "Java"
print(2programming_language)


# In[11]:


#shouldn't leave a space while giving variable name
p language = "java"


# In[12]:


#variable name shouldnot contain any special characters
language& = "program"
print(language&)


# In[14]:


#printing by combining two statements
print("Hi Students "+"Welcome to Python Programming")


# In[2]:


#shouldnot take a integer with string while concatinating
room_no = 5
print("Hi Students "+"Welcome to Python Programming "+"this is room no"+room_no)


# In[20]:


# use of f-string
print(f"Hi Students, Welcome to Python Programming. This is room number {room_no}")


# In[25]:


#printing using f-string
Name = "Ankitha"
age = 23
percentage = 90
print(f'Hi, My name is {Name}, my age is {age} and I got {percentage} percentage')


# In[26]:


#printing with variables

name = "Codegnan"
location = "Hyderabad"
branch = 5
print(name,location,branch)


# In[31]:


#commenting multiple-lines and single line
'''name = "Codegnan"
branchABC = 5'''
#print(name,branch)


# In[32]:


#swapping two numbers without third variable
x = 10
y = 20
print(x,y)
x,y = y,x
print(x,y)


# In[33]:


#swapping two numbers with third variale
x = 100
y = 200
print(x,y)
temp = x
x = y
y = temp
print(x,y)

