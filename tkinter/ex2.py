#%%
import tkinter as tk
import numpy as np
import matplotlib as mpl
import sys
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
#%%
#create a new application gui
#application inherits from tk.Frame
class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)  #using super, so no need for explicit init of parent, tk.Frame
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.run = tk.Button(self,text="RUN",fg="green",command=self.run)
        self.run.pack(side="left")

        self.stop = tk.Button(self, text="STOP", fg="red",command=self.stop)
        self.stop.pack(side="right")
        
        self.canvas_w=300
        self.canvas_h=100
        self.canvas =tk.Canvas(self,width=self.canvas_w,height=self.canvas_h)
        self.canvas.pack(side='bottom')
    
    def create_figure(self,X,Y):
        self.fig = mpl.figure.Figure(figsize=(2, 1))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.plot(X, Y)
        self.fig_x, self.fig_y = 100, 100
        fig_photo = Application.draw_figure()
        self.fig_w, self.fig_h = fig_photo.width(), fig_photo.height()
    
    def draw_figure(self):
        figure_canvas_agg = FigureCanvasAgg(self.fig)
        figure_canvas_agg.draw()
        figure_x, figure_y, figure_w, figure_h = self.fig.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = tk.PhotoImage(master=self.canvas, width=figure_w, height=figure_h)
    
        # Position: convert from top-left anchor to center anchor
        self.canvas.create_image(self.fig_x + figure_w/2, self.fig_y + figure_h/2, image=photo)
    
        # Unfortunately, there's no accessor for the pointer to the native renderer
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    
        # Return a handle which contains a reference to the photo object
        # which must be kept live or else the picture disappears
        return photo
    

    def run(self):
        print("run!")
    
    def stop(self):
        print("stop!")

root = tk.Tk()
root.geometry("600x600")
app = Application(master=root)
X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)
app.create_figure(X,Y)
app.mainloop()