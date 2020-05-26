#%%
import numpy as np
import open3d
import pandas as pd
import pcl_reader
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from matplotlib import cm
import glob
import time

#%%
PCLreader=pcl_reader.PCLReader()
myPCD=PCLreader.read_pcl("260675211284.pcd")
#%%
myPCDfilt=myPCD[np.isfinite(myPCD['z'])]
myPCDarray=myPCDfilt.values
x=myPCDarray[:,0]
y=myPCDarray[:,1]
z=myPCDarray[:,2]
#%%
""" fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show() """
#%%
#create grid: x,y,z
print('min x=',x.min())
print('max x=', x.max())
print('min y=',y.min())
print('max y=', y.max())
print('min z=',z.min())
print('max z=', z.max())
#%%
print(np.ceil(x.min()))
print(np.floor(x.max()))
print(np.ceil(y.min()))
print(np.floor(y.max()))
print(np.ceil(z.min()))
print(np.floor(z.max()))
#%%
xmin=np.ceil(x.min())
xmax=np.floor(x.max())
ymin=np.ceil(y.min())
ymax=np.floor(y.max())
zmin=np.ceil(z.min())
zmax=np.floor(z.max())
normalized = (z-min(z))/(max(z)-min(z))

#grid_x, grid_y = np.mgrid[xmin:xmax, ymin:ymax]
grid_x, grid_y = np.mgrid[-100:100, -50:50]
grid_z1=griddata(myPCDarray[:,0:2],normalized,(grid_x,grid_y),method='linear')

#%%
cm = plt.get_cmap("plasma")
plt.style.use('dark_background')
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(211,projection='3d')
#surf = ax.plot_wireframe(grid_x, grid_y, grid_z1,color='black')
#surf = ax.plot_surface(grid_x, grid_y, grid_z1,cmap='hot',vmin=0,vmax=1,rstride=1, cstride=1, antialiased=True, shade=True)
surf = ax.contourf(grid_x, grid_y, grid_z1, levels=50, cmap='hot')
#ax.view_init(80,120)
ax._axis3don=False

#%%
ax = fig.add_subplot(212)
ax.set_axis_off()
CS = ax.contourf(grid_x, grid_y, grid_z1, levels=25,cmap='hot')
#ax.clabel(CS, inline=1, fontsize=10)
#ax.set_title('Simplest default with labels')
#plt.ion()
plt.show()

