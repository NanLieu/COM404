from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.bike_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\bike.gif")
        
        # set window attributes
        self.configure(height=550,
                       width=550)

        # set animation attributes
        self.bike_x_pos = 0
        self.bike_y_pos = 250
        self.bike_x_change = 1
        self.bike_y_change = -1
        
        # add components
        self.add_bike_image_label() 
        
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
        self.after(5, self.tick)

    # the bike image
    def add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.place(x=self.bike_x_pos,
                                    y=self.bike_y_pos)
        self.bike_image_label.configure(image=self.bike_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 