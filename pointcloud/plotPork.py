import numpy as np
import open3d
import pandas as pd
import pcl_reader
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from matplotlib import cm
import matplotlib
import glob
import time

class plotPork(object):
    def __init__(self):
        self.reader=pcl_reader.PCLReader()
        self.grid_x, self.grid_y = np.mgrid[-100:100:1, -50:50:1]
        plt.style.use('dark_background')
        self.fig=plt.figure()
        self.ax3d = self.fig.add_subplot(211,projection='3d')
        self.ax3d.set_zlim3d( -1, 1 )
        self.ax3d._axis3don=False
        self.ax3d.view_init(80,140)
        z = np.zeros( self.grid_x.shape )
        #self.surf = self.ax.plot_surface(self.grid_x, self.grid_y, z,cmap='hot',
        #vmin=0,vmax=1,rstride=1, cstride=1, antialiased=True, shade=True)\
        self.surf = self.ax3d.contourf(self.grid_x, self.grid_y, z, levels=50, cmap='hot')
        
        self.ax2d = self.fig.add_subplot(212)
        self.ax2d.set_axis_off()
        self.cs=self.ax2d.contourf(self.grid_x, self.grid_y, z, levels=25,cmap='hot')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        
    def drawNow(self,fname):
        myPCD=self.reader.read_pcl(fname)
        myPCDfilt=myPCD[np.isfinite(myPCD['z'])]
        myPCDarray=myPCDfilt.values
        #x=myPCDarray[:,0]
        #y=myPCDarray[:,1]
        z=myPCDarray[:,2]
        normalized = (z-min(z))/(max(z)-min(z))
        z_new=griddata(myPCDarray[:,0:2],normalized,(self.grid_x,self.grid_y),method='linear')
        #self.surf.remove()
        for s3 in self.surf.collections:
            s3.remove()
        self.surf = self.ax3d.contourf(self.grid_x, self.grid_y, z_new, levels=50, cmap='hot')
        #self.cs.remove()
        for s2 in self.cs.collections:
            s2.remove()
        self.cs=self.ax2d.contourf(self.grid_x, self.grid_y, z_new, levels=25,cmap='hot')
        #self.surf = self.ax.plot_surface(self.grid_x, self.grid_y, z_new,cmap='hot',
        #vmin=0.5,vmax=1,rstride=1, cstride=1, antialiased=True, shade=True,alpha=1)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

def unitTest():
    matplotlib.interactive(True)
    myPork=plotPork()
    files=glob.glob('/home/caden/Documents/SoftwareDev/pork/newData/Up3/*.pcd')
    #files=glob.glob('*.pcd')
    for file in files:
        myPork.drawNow(file)
        time.sleep(0.5)

if __name__ == "__main__":
    unitTest()


