#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sum(a,b):
  if((a*b)<=1000):
    return a*b
  else:
    return a+b
  



a=int(input('enter a number'))
b=int(input('enter a number'))
print(sum(a,b))


# In[5]:


sum=0
n=int(input('enter a value for n'))
for i in range(1,n+1):
    sum=sum+i
print("sum of",n,"numbers is",sum)


# In[9]:


n=int(input('enter a number'))
c=0
s=n
while s!=0:
    c=c+1
    s=s//10
print('the number of digits in',n,'is',c)


# In[11]:


str=input('enter a string')
print(str[::2])


# In[15]:


def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
    
a=int(input('enter the starting value of interval')) 
b=int(input('enter the ending value of interval'))
for i in range(a,b+1):
    if(isprime(i)):
        print(i)
        
        


# In[ ]:




