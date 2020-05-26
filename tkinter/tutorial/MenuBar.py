#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:01:29 2019

@author: caden
"""
import tkinter as tk

#%%
#Define master widget
class Window(tk.Frame): #Window inherits from frame... Window is a frame
    def __init__(self,master):
        tk.Frame.__init__(self,master=None)
        self.master=master
        self.init_window()
        
    def init_window(self):
        #change title
        self.master.title('GUI')
        #fill entire root window with widget
        self.pack(fill=tk.BOTH,expand=1)
        #create button instance
        quitButton=tk.Button(self,text='Quit',command=self.client_exit)
        #place the button
        quitButton.place(x=0,y=0)
        
        #create menu instance
        myMenu=tk.Menu(self.master) 
        #add the menu to the app
        self.master.config(menu=myMenu) 
        #create a file object
        Exit=tk.Menu(myMenu)
        #call back
        Exit.add_command(label='Exit',command=self.client_exit)
        #add file to the menu
        myMenu.add_cascade(label='Exit',menu=Exit)
        #Create edit object
        Undo=tk.Menu(myMenu)
        Undo.add_command(label='Undo')
        myMenu.add_cascade(label='Undo',menu=Undo)
        
        
    
    def client_exit(self):
        exit()
        
        


#%% Create gui as myApp
myApp=tk.Tk()
myApp.geometry("400x300") #size

#%%configure the gui
app=Window(myApp)

#%% launch the gui
myApp.mainloop()
