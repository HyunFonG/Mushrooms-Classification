import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side="bottom")
        self.initialize()

    def initialize(self):
        global entryText
        global cap_shape

        self.init_cap_shape()


        self.cap_surface_frame = tk.Frame(root)
        self.cap_surface_frame.pack(side="top")
        self.cap_surface = tk.StringVar("")

        self.cap_surface_frame = tk.Frame(root)
        self.cap_surface_frame.pack(side="top")
        self.cap_surface = tk.StringVar("")
        
    
        self.label = tk.Label(self.cap_surface_frame, text="cap surface:")
        self.label.pack(side="left")

        self.item = tk.OptionMenu(self.cap_surface_frame, self.cap_surface, "fibrous", "grooves", "scaly", "smooth")
        self.item.pack(side="top")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def init_cap_shape(self):
        self.cap_shape_frame = tk.Frame(root)
        self.cap_shape_frame.pack(side="top")
        self.cap_shape = tk.IntVar()

        self.item = tk.Radiobutton(self.cap_shape_frame, text="bell", value=1, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")
        self.item = tk.Radiobutton(self.cap_shape_frame, text="conical", value=2, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")
        self.item = tk.Radiobutton(self.cap_shape_frame, text="convex", value=3, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")
        self.item = tk.Radiobutton(self.cap_shape_frame, text="flat", value=4, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")
        self.item = tk.Radiobutton(self.cap_shape_frame, text="knobbed", value=5, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")
        self.item = tk.Radiobutton(self.cap_shape_frame, text="sunken", value=6, variable=self.cap_shape)
        self.item.pack(side="top", anchor="w", padx="10")

    def init_cap_surface(self):
        print ("")

    def init_cap_color(self):
        print("")

    def say_hi(self):
        print("hi there, everyone!")
        print(self.cap_surface.get())

if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()