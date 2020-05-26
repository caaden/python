#%%
import tkinter as tk
from PIL import Image
from PIL import ImageTk


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
        Edit=tk.Menu(myMenu)
        Edit.add_command(label='Show Image',command=self.showImg)
        Edit.add_command(label='Show Text',command=self.showText)
        myMenu.add_cascade(label='Edit',menu=Edit)
    
    def showImg(self):
        load=Image.open("chat.png")
        render=ImageTk.PhotoImage(load)
        img=tk.Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

    def showText(self):
        text=tk.Label(self, text="This is my text.")
        text.pack()
        
        
    def client_exit(self):
        exit()
        

#%% Create gui as myApp
myApp=tk.Tk()
myApp.geometry("400x300") #size

#%%configure the gui
app=Window(myApp)

#%% launch the gui
myApp.mainloop()
