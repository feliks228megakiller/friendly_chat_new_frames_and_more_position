import customtkinter as ctk
import modules.create_frame as m_frame
#
class App(ctk.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        #
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Головне вікно програми")
        self.FRAME1 = m_frame.My_Frame(text= "Friendly Chat", 
                                       master = self, 
                                       width= 130, 
                                       height= app_height - 20, 
                                       border_width= 5)
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        self.FRAME2 = m_frame.My_Frame(text = "Чати", 
                                       master = self, 
                                       width= 130, 
                                       height= app_height - 20, 
                                       border_width= 5)
        
        self.FRAME1.grid(row = 0, column = 0, padx = 20, pady = 10)
        # self.FRAME.pack(padx= 10, pady = 10, expand = True)
        self.FRAME2.place(relx = 0.19, rely= 0.017, anchor = ctk.NW)

main_app = App(800, 600)