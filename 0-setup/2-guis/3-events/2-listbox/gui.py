from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Song Maker")
        self.configure(bg="#ccc", padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_lyrics_label()
        self.__add_lyrics_entry()
        self.__add_dropdown_label()
        self.__add_dropdown_entry()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.pack(fill=X)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.pack(fill=X)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Song Maker")
    
    def __add_lyrics_label(self):
        pass
    
    def __add_lyrics_entry(self):
        pass
    
    def __add_dropdown_label(self):
        pass

    def __add_dropdown_entry(self):
        pass


