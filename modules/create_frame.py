import customtkinter as ctk 

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, **kwargs):
        super().__init__(master = master,width = width, height = height, border_width = border_width, **kwargs)
        self.LABEL1 = ctk.CTkLabel(self, text= text)
        self.LABEL1.place(relx = 0.2, rely = 0.01, anchor = ctk.NW)
        self.LABEL2 = ctk.CTkLabel(self, text= text)
        self.LABEL2.place(relx = 1.0, rely = 0.01, anchor = ctk.NW)