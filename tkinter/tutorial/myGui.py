#%%
import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

#%%
#Define master widget
class Window(tk.Frame): #Window inherits from frame... Window is a frame
    def __init__(self,master):
        tk.Frame.__init__(self,master=None)
        self.master=master
        self.init_window()
        self.draw_figure()
        self.update_data()
        
    def init_window(self):
        #change title
        self.master.title('GUI')
        #fill entire root window with widget
        self.pack(fill=tk.BOTH,expand=1)
        #create button
        quitButton=tk.Button(self,text='Quit',command=self.client_exit)
        quitButton.pack(side=tk.TOP)
        
    def draw_figure(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        x = np.linspace(0, 6*np.pi, 100)
        y = np.sin(x)
        self.line1,=self.fig.add_subplot(111).plot(x,y,'r-')
        canvas = FigureCanvasTkAgg(self.fig, self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)
    
    def update_data(self):
        x = np.linspace(0, 6*np.pi, 100)
        for phase in np.linspace(0, 10*np.pi, 500):
            self.line1.set_ydata(np.sin(x + phase))
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
        
        
        
    def client_exit(self):
        exit()
        
        


#%% Create gui as myApp
myApp=tk.Tk()
myApp.geometry("400x300") #size

#%%configure the gui
app=Window(myApp)

#%% launch the gui
myApp.mainloop()