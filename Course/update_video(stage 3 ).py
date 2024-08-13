import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import video_library as lib
import font_manager as fonts
from video_library import VideoLibrary

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class update_video:
    def __init__(self,window):
        window.geometry("600x300")
        window.title("Update Video")
        self.videolibrary = VideoLibrary()

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.key_input_txt = tk.Entry(window, width=3)
        self.key_input_txt.grid(row=0, column=2, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Rating")
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.rating_input_txt = tk.Entry(window, width=3)
        self.rating_input_txt.grid(row=1, column=2, padx=10, pady=10)

        update_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)
        update_btn.grid(row=0, column=4, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.Text(window, width=35, height=8, wrap="none")
        self.list_txt.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def update_display(self):  
        key = self.key_input_txt.get()
        name = self.videolibrary.get_name(key)
        director = self.videolibrary.get_director(key) 
        rating = self.videolibrary.get_rating(key)
        video_details = f"{name}\n{director}\nrating: {rating}"
        set_text(self.list_txt, video_details)

    def update_video_clicked(self): 
        key = self.key_input_txt.get()
        try:
            rating = int(self.rating_input_txt.get())
            if rating >=0 and rating <=5:
                self.videolibrary.set_rating(key, rating)
            else:
                messagebox.showerror("Error", "Please enter 0-5 rating")
        except:
            messagebox.showerror("Error", "Please enter 0-5 rating")
        self.update_display()
        self.status_lbl.configure(text="Update Videos button was clicked!")

    def check_video_clicked(self):
        key = self.key_input_txt.get()
        name = VideoLibrary().get_name(key)
        if name is not None:
            director = self.videolibrary.get_director(key) 
            rating = self.videolibrary.get_rating(key)
            video_details = f"{name}\n{director}\nrating: {rating}"
            set_text(self.list_txt, video_details)
        elif name is None:
            set_text(self.list_txt, "Please enter valid number")
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

if __name__ == "__main__":  
    window = tk.Tk()        
    fonts.configure()       
    update_video(window)    
    window.mainloop()       