#%%
import tkinter as tk
import numpy as np
import pandas as pd
import glob
import time
import matplotlib

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import cm
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

import pcl_reader


#%%
#Define master widget
class Window(tk.Frame): #Window inherits from frame... Window is a frame
    def __init__(self,master):
        tk.Frame.__init__(self,master=None)
        self.configure(background='black')
        self.master=master
        self.master.configure(background='black')
        self.init_window()
        self.draw_figure()
        self.reader=pcl_reader.PCLReader()
        
    def init_window(self):
        #change title
        self.master.title('fringeAI Pork Test')
        #fill entire root window with widget
        self.pack(fill=tk.BOTH,expand=1)
        
        #create quit button
        quitButton=tk.Button(self,text='Quit',command=self.client_exit)
        quitButton.pack(side=tk.LEFT)
        #create update button
        updateButton=tk.Button(self,text='Run',command=self.update_data)
        updateButton.pack(side=tk.LEFT)
        self.arrowCanvas=tk.Canvas(self,height=50, width=100,bg='black',bd=0)
        self.arrowCanvas.config(highlightbackground='black')
        self.arrowCanvas.pack(side=tk.RIGHT)       
    
    def drawArrow(self):
        self.myArrow=self.arrowCanvas.create_polygon(0,0,100,0,50,50,fill='green')

    def removeArrow(self):
        self.arrowCanvas.delete(self.myArrow)    
        
    def draw_figure(self):
        plt.style.use('dark_background')
        self.fig = Figure()
        self.grid_x, self.grid_y = np.mgrid[-100:100:1, -100:100:1]
        self.ax2d = self.fig.gca()
        self.ax2d.set_aspect('equal')
        self.ax2d.set_axis_off()
        z = np.ones( self.grid_x.shape )
        self.cs=self.ax2d.contourf(self.grid_x, self.grid_y, z, levels=1,cmap='hot')
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
      
    def update_data(self):
        files= glob.glob('/home/caden/Documents/SoftwareDev/pork/newData/Up3/*.pcd')
        #files=glob.glob('/home/caden/Documents/SoftwareDev/pork/newData/*.pcd')
        for file in files: 
            try:
                self.removeArrow()
                self.arrowCanvas.after(20)
                self.arrowCanvas.update() 
            except:
                pass   
            myPCD=self.reader.read_pcl(file)
            myPCDfilt=myPCD[np.isfinite(myPCD['z'])]
            myPCDarray=myPCDfilt.values
            #x=myPCDarray[:,0]
            #y=myPCDarray[:,1]
            z=myPCDarray[:,2]
            normalized = (z-min(z))/(max(z)-min(z))
            z_new=griddata(myPCDarray[:,0:2],normalized,(self.grid_x,self.grid_y),method='linear')
            for s2 in self.cs.collections:
                s2.remove()
            self.cs=self.ax2d.contourf(self.grid_x, self.grid_y, z_new, levels=50,cmap='hot')
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
            self.drawArrow()
            self.arrowCanvas.after(20)
            self.arrowCanvas.update()
            
        
    def client_exit(self):
        exit()
        
        
def unitTest():
    myApp=tk.Tk()
    myApp.geometry("640x480")
    app=Window(myApp)
    myApp.mainloop()

if __name__=="__main__":
    unitTest()