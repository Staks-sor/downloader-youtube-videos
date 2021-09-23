from tkinter import filedialog
from tkinter import *
from pytube import YouTube
import os

root = Tk()
root.geometry("500x350")
root.resizable(0, 0)
root.config(bg="gray22")
root.title("YouTube Video Downloader")
root.iconbitmap("youtube.ico")


def Downloader():

    url = YouTube(str(link.get()))
    video = (
        url.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    video.download("C:/Users/stass/OneDrive/Documents/python/youtube/videos")
    Label(root, text="DOWNLOADED", font="arial 15").place(x=180, y=230)


Label(root, text="Staks edition", font="arial 10 bold", bg="gray22", fg="pink").place(
    x=30, y=10
)


link = StringVar()

Label(root, text="Ведите URL адрес:", font="arial 15 bold", bg="gray22").place(
    x=160, y=40
)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=80)

Button(
    root, text="DOWNLOAD", font="arial 15 bold", bg="pink", padx=2, command=Downloader
).place(x=180, y=280)


root.mainloop()
