#!/usr/bin/env python
# coding: utf-8

# # Find the value of the following questions, Where x=5

# In[14]:


x=5
y=((2*x)+5)/((x*x)+(5*x)+6)
print("The answer is : ",y)
y=((x*x)+(5*x)+6)/((2*x)+5)
print("The answer is : ",y)
# (2x-3)(x-9)
y=(2*x*x)-(18*x)-(3*x)+(27)
print("The answer is : ",y)


# # Create a username and password login file using nested while loop

# In[1]:


import sys
print(" Welcome to our service : ")
x = y = z = 0
while x<1:
    if z<1:
        a=input("Enter your user name : ")
        if a == "ankit":
            while y<5:
                b=input("Enter your password : ")
                if b == "demo":
                    print("******* OH!!! You Are Back!!! *******") 
                    z=z+1
                    break
                else:
                    print("####### Wrong Answer #######")
                    y=y+1
            else:
                 print("XXXXXXXX    You are blocked    XXXXXXXX")
        else:
            print("******* Wrong User Name!!!  *******")
            x=x+1
    else:
        print("*****   See You Later   *****")
        break
else:
    print("XXXXXXXX    Try with a different name or signup!!!   XXXXXXXX")
        


# In[ ]:




