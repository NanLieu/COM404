from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()

    
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)
        
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(   bg="#eee",
                                        font="Arial 18",
                                        text="Entrance Ticket")
        
        
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.instruction_label.configure(   bg="#eee",
                                            font="Arial 10",
                                            text="How many tickets are needed?",
                                            padx=10,
                                            pady=10)
        
    def __add_tickets_entry(self):
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        self.email_entry.configure(width=40)
        
    def __add_buy_button(self):
        self.buy_button = Button(self.outer_frame)
        self.buy_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.buy_button.configure(      bg="#eee",
                                        text="Buy",
                                        padx=20)