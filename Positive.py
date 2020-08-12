#!/usr/bin/env python
# coding: utf-8

# In[1]:


def positive(list1):
    for i in list1:
        if i>=0:
            print(i ,end=" ")

list1 = [12,-7,5,64,-14]
list2 =[12,14,-95,3]
print("list1=" , list1)
positive(list1)
print()
print("list2=" , list2)
positive(list2)


# In[ ]:




