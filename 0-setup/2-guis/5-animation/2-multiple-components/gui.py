from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.bike_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\bike.gif")
        self.ambulance_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\ambulance.gif")
        
        # set window attributes
        self.configure(height=550,
                       width=550)

        # set animation attributes
        self.bike_x_pos = 0
        self.bike_y_pos = 400
        self.bike_x_change = 1
        self.bike_y_change = -1
        self.ambulance_x_pos = 500
        self.ambulance_y_pos = 300
        self.ambulance_x_change = -1
        self.ambulance_y_change = -1
        
        # add components
        self.add_bike_image_label()
        self.add_ambulance_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if (self.bike_x_pos > 500):
            self.bike_x_change = -1
        elif (self.bike_x_pos < 0):
            self.bike_x_change = 1
        if (self.bike_y_pos > 500):
            self.bike_y_change = -1
        elif (self.bike_y_pos < 0):
            self.bike_y_change = 1
        self.bike_x_pos = self.bike_x_pos + self.bike_x_change
        self.bike_y_pos = self.bike_y_pos + self.bike_y_change
        self.bike_image_label.place(x=self.bike_x_pos, 
                                    y=self.bike_y_pos)
        if (self.ambulance_x_pos > 500):
            self.ambulance_x_change = -1
        elif (self.ambulance_x_pos < 0):
            self.ambulance_x_change = 1
        if (self.ambulance_y_pos > 500):
            self.ambulance_y_change = -1
        elif (self.ambulance_y_pos < 0):
            self.ambulance_y_change = 1
        self.ambulance_x_pos = self.ambulance_x_pos + self.ambulance_x_change
        self.ambulance_y_pos = self.ambulance_y_pos + self.ambulance_y_change
        self.ambulance_image_label.place(x=self.ambulance_x_pos, 
                                    y=self.ambulance_y_pos)
    
        self.after(4, self.tick)

    # the bike image
    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.place(x=self.bike_x_pos,
                                    y=self.bike_y_pos)
        self.bike_image_label.configure(image=self.bike_image)
    
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.place(x=self.ambulance_x_pos,
                                    y=self.ambulance_y_pos)
        self.ambulance_image_label.configure(image=self.ambulance_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 