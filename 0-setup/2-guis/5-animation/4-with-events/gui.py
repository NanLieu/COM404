from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.plane_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\plane.gif")
        
        # set window attributes
        self.configure(height=600,
                       width=800)

        # set animation attributes
        self.plane_x_pos = 0
        self.plane_y_pos = 250
        self.plane_x_change = 1
        self.plane_y_change = -1
        
        # add components
        self.add_plane_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if (self.plane_x_pos > 750):
            self.plane_x_change = -1
        elif (self.plane_x_pos < 0):
            self.plane_x_change = 1
        if (self.plane_y_pos > 400):
            self.plane_y_change = -1
        elif (self.plane_y_pos < 50):
            self.plane_y_change = 1
        self.plane_x_pos = self.plane_x_pos + self.plane_x_change
        self.plane_y_pos = self.plane_y_pos + self.plane_y_change
        self.plane_image_label.place(x=self.plane_x_pos, 
                                    y=self.plane_y_pos)
        self.after(5, self.tick)

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