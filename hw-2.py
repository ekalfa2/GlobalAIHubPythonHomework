#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name=str(input("Enter your first name\n"))
lastname=str(input("Enter your last name\n"))
age=int(input("Enter your age\n"))
dateyear=int(input("Enter your date of birth(just year)\n"))
my_list=[name,lastname,age,dateyear]
for list in my_list:
  print(list)
if (age <18):
    print("You can't go out because it's too dangerous")
elif (age>18):
    print("You can go out to the street")

