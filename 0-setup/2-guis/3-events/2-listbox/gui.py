from tkinter import *
from tkinter import messagebox

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
        self.__add_song_button()
        self.__add_listbox_label()
        self.__add_lyrics_listbox()



    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Song Maker")
    
    def __add_lyrics_label(self):
        self.lyrics_label = Label(self.outer_frame)
        self.lyrics_label.grid(row=1, column=0, sticky=W)
        self.lyrics_label.configure(    bg="#eee",
                                        text="Lyrics to add:")

    
    def __add_lyrics_entry(self):
        self.lyrics_entry = Entry(self.outer_frame)
        self.lyrics_entry.grid(row=2, column=0)
        self.lyrics_entry.configure(width=30)

    def __add_song_button(self):
        self.song_button = Button(self.outer_frame)
        self.song_button.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
        self.song_button.configure(      bg="#eee",
                                        text="Add",
                                        padx=20)
        self.song_button.bind("<ButtonRelease-1>", self.__song_button_clicked)
    
    
    def __add_listbox_label(self):
        self.listbox_label = Label(self.outer_frame)
        self.listbox_label.grid(row=3, column=0, sticky=W)
        self.listbox_label.configure(    bg="#eee",
                                        text="Lyrics:")

    def __add_lyrics_listbox(self):
        self.lyrics_listbox = Listbox(self.outer_frame)
        self.lyrics_listbox.grid(row=4, column=0, columnspan=2)
        self.lyrics_listbox.configure(width=45)

    def __song_button_clicked(self, event):
        add_lyrics = self.lyrics_entry.get()
        self.lyrics_listbox.insert(END, add_lyrics)

