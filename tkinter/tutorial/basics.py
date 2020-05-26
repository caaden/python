#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:01:29 2019

@author: caden
"""
import tkinter as tk

#%%
#Define master widget
class Window(tk.Frame): #Window inherits from frame
    def __init__(self,master=None): #input master is the 
        tk.Frame.__init__(self,master)
        self.master=master

#%%     
root=tk.Tk()
app=Window(root)
root.mainloop()