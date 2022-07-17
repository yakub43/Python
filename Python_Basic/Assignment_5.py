#!/usr/bin/env python
# coding: utf-8
1. What does an empty dictionary's code look like?
# In[1]:


d = {}
print(type(d))

2. What is the value of a dictionary value with the key 'foo' and the value 42?
# In[5]:


d = {"foo" : 42}
print(d["foo"])

3. What is the most significant distinction between a dictionary and a list?Most significant difference is that, Dictionary stores it's values with key value pair, where list stores directly value.
Example:
       Dictionary --> student = {1:"john", 2:"james", 3: "jane"}
       List       --> fruits = ["Mango", "Banana", "Cherry", "Strawberry"]4. What happens if you try to access spam["foo"] if spam is {"bar": 100}?
# In[6]:


spam = {"bar" : 100}
print(spam["foo"]) # This will return error as we are trying to access the element with key (foo) which is not present in dict

5. If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and
"cat" in spam.keys()?
# In[7]:


spam = {"Cat" : "Cat"}
print(spam.keys())
# Here we have same for the key as well as for the value, so when we try to access the value it will return cat

6. If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and
"cat" in spam.values()?
# In[8]:


spam = {"cat" : "cat"}
print(spam.values())
# Here we are trying to return the values present in dictionary

7. What is a shortcut for the following code?
if "color" not in spam:
spam["color"] = "black"
# In[1]:


spam = {}
spam.setdefault("color","black")

8. How do you pretty print dictionary values using which module and function?we use pprint() module to use pretty print dictionary
# In[5]:


#Example
fruit = {"Citric":["Orange","Lemon","Strawberry"],"Sweet":["Banana","Apple","Chiku"]}
print("Using print ")
print(fruit)

print()

import pprint
print("using pretty print function")
print()
pprint.pprint(fruit)


# In[ ]:




