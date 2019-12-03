from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.bike_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\bike.gif")
        self.ambulance_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\ambulance.gif")
        self.plane_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\plane.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.bike_x_pos = 0
        self.bike_y_pos = 100
        self.bike_x_change = 1
        self.bike_y_change = 0
        self.ambulance_x_pos = 0
        self.ambulance_y_pos = 250
        self.ambulance_x_change = 1
        self.ambulance_y_change = 0
        self.plane_x_pos = 0
        self.plane_y_pos = 400
        self.plane_x_change = 1
        self.plane_y_change = 0
        self.num_ticks = 0
        
        
        
        
        # add components
        self.add_bike_image_label()
        self.add_ambulance_image_label() 
        self.add_plane_image_label()
        
        # start the timer
        self.tick()
        
        
    # the timer tick function    
    def tick(self):
        self.num_ticks = self.num_ticks + 1
        if (self.num_ticks % 30 == 0):
            if (self.bike_x_pos > 450):
                self.bike_x_change = -1
            elif (self.bike_x_pos < 0):
                self.bike_x_change = 1

            self.bike_x_pos = self.bike_x_pos + self.bike_x_change
            self.bike_image_label.place(x=self.bike_x_pos)

        if (self.num_ticks % 10 == 0):
            if (self.ambulance_x_pos > 450):
                self.ambulance_x_change = -1
            elif (self.ambulance_x_pos < 0):
                self.ambulance_x_change = 1

            self.ambulance_x_pos = self.ambulance_x_pos + self.ambulance_x_change
            self.ambulance_image_label.place(x=self.ambulance_x_pos)
        
        if (self.num_ticks % 1 == 0):
            if (self.plane_x_pos > 450):
                self.plane_x_change = -1
            elif (self.plane_x_pos < 0):
                self.plane_x_change = 1

            self.plane_x_pos = self.plane_x_pos + self.plane_x_change
            self.plane_image_label.place(x=self.plane_x_pos)

        
        self.after(1, self.tick)

    # the bike image
    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.place(x=self.bike_x_pos,
                                    y=self.bike_y_pos)
        self.bike_image_label.configure(image=self.bike_image)
    # the ambulance image
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.place(x=self.ambulance_x_pos,
                                    y=self.ambulance_y_pos)
        self.ambulance_image_label.configure(image=self.ambulance_image)
    # the plane image
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.place(x=self.plane_x_pos,
                                    y=self.plane_y_pos)
        self.plane_image_label.configure(image=self.plane_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 