from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
    	 # load resources
        self.cactus_image = PhotoImage(file="U:/Documents/COM404 Repository/COM404/cactus.gif")
        self.flipped_cactus_image = PhotoImage(file="U:/Documents/COM404 Repository/COM404/flipout cactus.gif")

        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_cactus_header()
        self.__add_cactus_image_label()
        self.__add_cactus_flip_button()

    def __add_cactus_header(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=1, columnspan=3)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Cactus")
        
    def __add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=1)
        self.cactus_image_label.configure(image=self.cactus_image,
                                             height=500,
                                             width=500)

    def __add_cactus_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=1, columnspan=1, pady=10)
        self.flip_button.configure(      bg="#eee",
                                        text="Flip!",
                                        padx=20)
        self.flip_button.bind("<ButtonRelease-1>", self.__flip_button_clicked)
    
    def __flip_button_clicked(self, event):
        self.cactus_image_label.configure(image = self.flipped_cactus_image)
    



# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()