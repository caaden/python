#%%
import tkinter as tk
#%%
#create a new application guiz
class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.run = tk.Button(self,text="RUN",fg="green",command=self.run)
        self.run.pack(side="left")

        self.stop = tk.Button(self, text="STOP", fg="red",command=self.stop)
        self.stop.pack(side="right")

    def run(self):
        print("run!")
    
    def stop(self):
        print("stop!")

root = tk.Tk()
root.geometry("300x300")
app = Application(master=root)
app.mainloop()