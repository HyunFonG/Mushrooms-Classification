import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.initialize()

    def initialize(self):
        global entryText
        global cap_shape

        self.cap_shape = tk.IntVar()
        self.cap_shape_item = tk.Radiobutton(self, text="bell", value=1, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
        # self.cap_shape_item.pack(side="top",anchor="w" )
        self.cap_shape_item = tk.Radiobutton(self, text="conical", value=2, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
        self.cap_shape_item = tk.Radiobutton(self, text="convex", value=3, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
        self.cap_shape_item = tk.Radiobutton(self, text="flat", value=4, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
        self.cap_shape_item = tk.Radiobutton(self, text="knobbed", value=5, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
        self.cap_shape_item = tk.Radiobutton(self, text="sunken", value=6, variable=self.cap_shape)
        self.cap_shape_item.pack(side="top", anchor="w", padx="10")
    
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        print(self.cap_shape.get())

if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()