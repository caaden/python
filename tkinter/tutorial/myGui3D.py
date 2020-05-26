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
        self.master=master
        self.init_window()
        self.draw_figure()
        self.reader=pcl_reader.PCLReader()
        
    def init_window(self):
        #change title
        self.master.title('GUI')
        #fill entire root window with widget
        self.pack(fill=tk.BOTH,expand=1)
        #create quit button
        quitButton=tk.Button(self,text='Quit',command=self.client_exit)
        quitButton.pack(side=tk.TOP)
        #create update button
        updateButton=tk.Button(self,text='Update',command=self.update_data)
        updateButton.pack(side=tk.TOP)
        
    def draw_figure(self):
        self.fig = Figure(figsize=(10, 4), dpi=100)
        self.grid_x, self.grid_y = np.mgrid[-100:100:1, -50:50:1]
        self.ax = self.fig.gca(projection='3d')
        self.ax.set_zlim3d( -1, 1 )
        self.ax._axis3don=False
        self.ax.view_init(20,140)
        z = np.zeros( self.grid_x.shape )
        self.surf = self.ax.plot_surface(self.grid_x, self.grid_y, z,cmap='coolwarm',
        vmin=-1,vmax=1,rstride=1, cstride=1, antialiased=True, shade=True)

        canvas = FigureCanvasTkAgg(self.fig, self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)
    
    def update_data(self):
        files= glob.glob('/home/caden/Documents/SoftwareDev/pork/newData/Up3/*.pcd')
        for file in files: 
            myPCD=self.reader.read_pcl(file)
            myPCDfilt=myPCD[np.isfinite(myPCD['z'])]
            myPCDarray=myPCDfilt.values
            #x=myPCDarray[:,0]
            #y=myPCDarray[:,1]
            z=myPCDarray[:,2]
            normalized = (z-min(z))/(max(z)-min(z))
            z_new=griddata(myPCDarray[:,0:2],normalized,(self.grid_x,self.grid_y),method='linear')
            self.surf.remove()
            self.surf = self.ax.plot_surface(self.grid_x, self.grid_y, z_new,cmap='coolwarm',
            vmin=0.5,vmax=1,rstride=1, cstride=1, antialiased=True, shade=True,edgecolor='none',alpha=1)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
            time.sleep(0.5)
        
    def client_exit(self):
        exit()
        
        
def unitTest():
    myApp=tk.Tk()
    myApp.geometry("400x300")
    app=Window(myApp)
    myApp.mainloop()

if __name__=="__main__":
    unitTest()