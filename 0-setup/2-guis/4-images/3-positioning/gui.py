from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
    
            # load resources
        self.map_image = PhotoImage(file="city-map.gif")
        self.bus_image = PhotoImage(file="bus2.gif")

            # set window attributes
        self.title("Gui")

        # add components
        self.__add_header_label()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()
    

    def __add_header_label(self):
        self.header_label = Label()
        self.header_label.grid(row=0, column=0)
        self.header_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Bus Journey")
    
    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure(width=800, height=800)

    def __add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)

    def __add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>", self.bus_move)

    def bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y))
        self.bus_image_label.place(x=event.x, y=event.y)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()