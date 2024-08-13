import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import video_library as lib
import font_manager as fonts
from video_library import VideoLibrary
from library_item import LibraryItem

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class Playlist:
    def __init__(self,window):
        window.geometry("800x400")
        window.title("Create Video List")
        self.videos = []
        self.position = 0
        self.videolibrary = VideoLibrary()

        Play_btn = tk.Button(window, text="Play", command=self.play_video_clicked)
        Play_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_btn = tk.Button(window, text="Add to playlist", command=self.add_video_clicked)
        add_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=54, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset playlist", command=self.reset_video_clicked)
        reset_btn.grid(row=2, column=3, padx=10, pady=10)


        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def show_video(self):
        key = self.videos[self.position]
        name = self.videolibrary.get_name(key)
        director = self.videolibrary.get_director(key) 
        rating = self.videolibrary.get_rating(key)
        video_details = f"{name}\n{director}\nrating: {rating}"
        set_text(self.video_txt, video_details)

        
    def add_video(self):
        key = self.input_txt.get()
        self.videos.append(key)
        output = self.videolibrary.list_videos(self.videos)
        set_text(self.list_txt, output)

    def update_playlist_display(self):
        output = self.videolibrary.list_videos(self.videos)
        set_text(self.list_txt, output)

    def play_all(self):
        if len(self.videos) == 0:
            messagebox.showerror("Error","NO VIDEOS IN THE PLAYLIST")
            return
        
        for key in self.videos:
            self.videolibrary.increment_play_count(key)

    def add_video_clicked(self):
        key = self.input_txt.get()
        name = self.videolibrary.get_name(key)
        if name is not None:
            self.add_video()
        else:
            messagebox.showerror("Error", "Please enter a valid number")
        self.status_lbl.configure(text = "Add button was clicked")

    def play_video_clicked(self):
        self.play_all()
        self.update_playlist_display()
        self.status_lbl.configure(text = "Play button was clicked")

    def reset_video_clicked(self):
        self.videos.clear()
        output = self.videolibrary.list_videos(self.videos)
        set_text(self.list_txt, output)
        self.status_lbl.configure(text = "Reset button was clicked")




if __name__ == "__main__":  
    window = tk.Tk()        
    fonts.configure()       
    Playlist(window)    
    window.mainloop()       