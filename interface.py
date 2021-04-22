#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:51:01 2018

@author: slipshod666
"""
import json
from tkinter import *
from minorprojectfinal import recommendations

def view_command(dataset):
    list1.delete(0,END)
    if grab_user_input() not in dataset:
        nouser="User not found"
        list1.insert(END,nouser)
    else:
        for row in recommendations(dataset,grab_user_input()):
            list1.insert(END,row)
def grab_user_input():
    userinput=user_text.get()
    return userinput
    

data_file = 'movieratings.json'
with open(data_file, 'r') as f:
    data = json.loads(f.read())
        
window=Tk()
window.title("Movie Recommender")

l1=Label(window,text="User")
l1.grid(row=0,column=0)

user_text=StringVar()
e1=Entry(window,textvariable=user_text)
e1.grid(row=0,column=1)

b1=Button(window,text="Recommendations",width=12,command=lambda:view_command(data))
b1.grid(row=9,column=0)

list1=Listbox(window,height=10,width=45)
list1.grid(row=1,column=0,rowspan=8,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=1,column=3,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()