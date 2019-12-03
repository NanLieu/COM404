from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.plane_image = PhotoImage(file="U:\Documents\COM404 Repository\COM404\\plane.gif")
        
        # set window attributes
        self.configure(height=550,
                       width=800)
        
        self.__add_up_button()
        self.__add_down_button()
        self.__add_straight_button()

        # set animation attributes
        self.plane_x_pos = 0
        self.plane_y_pos = 250
        self.plane_x_change = 1
        self.plane_y_change = 0
        
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

    def __add_up_button(self):
        self.up_button = Button()
        self.up_button.place(x=500, y=475)
        self.up_button.configure(      bg="#eee",
                                        text="Up",
                                        padx=20)
        self.up_button.bind("<ButtonRelease-1>", self.__up_button_clicked)

    def __add_down_button(self):
        self.down_button = Button()
        self.down_button.place(x=300, y=475)
        self.down_button.configure(      bg="#eee",
                                        text="Down",
                                        padx=20)
        self.down_button.bind("<ButtonRelease-1>", self.__down_button_clicked)
    
    def __add_straight_button(self):
        self.straight_button = Button()
        self.straight_button.place(x=400, y=475)
        self.straight_button.configure(      bg="#eee",
                                        text="Straight",
                                        padx=20)
        self.straight_button.bind("<ButtonRelease-1>", self.__straight_button_clicked)
        
    def __up_button_clicked(self, event):
        self.plane_y_change = -1
    
    def __down_button_clicked(self, event):
        self.plane_y_change = 1

    def __straight_button_clicked(self, event):
        self.plane_y_change = 0


        # the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 