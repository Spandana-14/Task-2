#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def positive(list):
    for i in list:
        if i>=0:
            print(i ,end=" ")

list=[]
n=int(input("Enter number of elemets:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
            

print("list=" , list)
positive(list)


# In[ ]:





# In[ ]:




