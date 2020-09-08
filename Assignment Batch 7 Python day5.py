#!/usr/bin/env python
# coding: utf-8

# # Question 1

# Write a program to identify sublist[2,5,6]is there in there in the given list in the same order, if yes, print its a match if not then print its Gone in function.
# 

# In[1]:


sbl = [2,5,6]

def checksublist(list1,list2):
    l1,l2 = list1[0], list2[0]
    
    for i in list2:
        if i not in list1:
            sbl = "its gone"
    else:
        sbl = "its a match"
    return sbl

list1 = [1,2,4,7,5,8,6,9,12]
list2 = [5,3,4,2,7,6,8,9,11]

print(checksublist(list1,list2))         
        
          


# # Question 2

# Make a function for prime Numbers and use Filter to filter out all the prime numbers from 1-2500

# In[5]:


def primeNumber(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True
lst = filter(primeNumber, range(1,2500))
print(list(lst))
    


# # Question 3

# Make a Lambda Function for capitalizing the whole sentence passed using arguments.
#  And map all the sentences in the list with the LambdaFunction

# In[3]:


char = ["Lets upgrade, is helping me to get back into eductaion!"]
char_new = map(lambda x: x.title(),char)
list(char_new)


# In[ ]:




