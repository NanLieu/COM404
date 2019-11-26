from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\ambulance.gif")
        self.bike_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\bike.gif")
        self.plane_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
        
    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=0, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def __add_bike_image_label():
        self.bike_image_label = Label1()
        self.bike_image_label.grid(row=0, column=2)
        self.bike_image_label.configure(image=self.bike_image,
                                        height=60,
                                        width=60)
 
    def __add_plane_image_label():
        self.plane_image_label = Label2()
        self.plane_image_label.grid(row=0, column=3)
        self.plane_image_label.configure(image=self.plane_image,
                                        height=60,
                                        width=60)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()