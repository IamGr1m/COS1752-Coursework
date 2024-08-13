import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class update_video:
    def __init__(self,window):
        window.geometry("600x300")
        window.title("Update Video")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Rating")
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=1, column=2, padx=10, pady=10)

        add_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)
        add_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=24, height=8, wrap="none")
        self.list_txt.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    
    def update_video_clicked(self):
        self.status_lbl.configure(text="Update Videos button was clicked!")

if __name__ == "__main__":  
    window = tk.Tk()        
    fonts.configure()       
    update_video(window)    
    window.mainloop()  