from tkinter import * 
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

    	 # load resources
        
        self.tick_image = PhotoImage(file="tick.gif")
        self.cross_image = PhotoImage(file="cross.gif")
    
      # add components
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_passport_label()
        self.__add_nights_label()
        self.__add_name_entry()
        self.__add_passport_entry()
        self.__add_nights_entry()
        self.__add_check_in_button()
        self.__add_name_image()
        self.__add_passport_image()
        self.__add_nights_image()

    def __add_heading_label(self):
        self.add_heading_label = Label()
        self.add_heading_label.grid(row=0, column=0, columnspan=2)
        self.add_heading_label.configure(   bg="#eee",
                                        font="Arial 16",
                                        text="Hotel Check In")
    def __add_name_label(self):
        self.add_name_label = Label()
        self.add_name_label.grid(row=1, column=0, sticky=W)
        self.add_name_label.configure(   bg="#eee",
                                        font="Arial 14",
                                        text="Name:")
    
    def __add_passport_label(self):
        self.add_passport_label = Label()
        self.add_passport_label.grid(row=2, column=0, sticky=W)
        self.add_passport_label.configure(   bg="#eee",
                                        font="Arial 14",
                                        text="Passport Number:")

    def __add_nights_label(self):
        self.add_nights_label = Label()
        self.add_nights_label.grid(row=3, column=0, sticky=W)
        self.add_nights_label.configure(   bg="#eee",
                                        font="Arial 14",
                                        text="No. of nights:")
    
    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)
        self.name_entry.configure(width=25)
    
    def __add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2, column=1)
        self.passport_entry.configure(width=25)
    
    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1)
        self.nights_entry.configure(width=25)

    def __add_check_in_button(self):
        self.check_in_button = Button()
        self.check_in_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.check_in_button.configure(      bg="#eee",
                                        text="Check In",
                                        padx=20)
        self.check_in_button.bind("<ButtonRelease-1>", self.__check_in_button_clicked)

    def __add_name_image(self):
        self.add_name_image = Label()
        self.add_name_image.grid(row=1, column=3)
        self.add_name_image.configure(image=self.cross_image,
                                             height=10,
                                             width=10)

    def __add_passport_image(self):
        self.add_passport_image = Label()
        self.add_passport_image.grid(row=2, column=3)
        self.add_passport_image.configure(image=self.cross_image,
                                             height=10,
                                             width=10)

    def __add_nights_image(self):
        self.add_nights_image = Label()
        self.add_nights_image.grid(row=3, column=3)
        self.add_nights_image.configure(image=self.cross_image,
                                             height=10,
                                             width=10)

    def __check_in_button_clicked(self, event):
        name_check = self.name_entry.get()
        passport_check = self.passport_entry.get()
        nights_check = self.nights_entry.get()
        nights = nights_check
        passport_number = passport_check

        if (name_check == ""):
            self.add_name_image.configure(image = self.cross_image)
        else:
            self.add_name_image.configure(image = self.tick_image)


        if (passport_check == ""):
            self.add_passport_image.configure(image = self.cross_image)
        else:
            passport_number = int(passport_check)
            if (passport_number == 0 or passport_number < 0):
                self.add_passport_image.configure(image = self.cross_image)
            else:
                self.add_passport_image.configure(image = self.tick_image)

        if (nights_check == ""):
            self.add_nights_image.configure(image = self.cross_image)
        else:
            nights = int(nights_check)
            if (nights == 0 or nights < 0):
                self.add_nights_image.configure(image = self.cross_image)
            else:
                self.add_nights_image.configure(image = self.tick_image)


# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()