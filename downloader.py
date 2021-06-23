from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.filedialog as fmsg
import os
import youtube_dl


def browserdir():
    download_directory = fmsg.askdirectory(initialdir=os.getcwd())
    directory.set(download_directory)


def my_hook(d):

    if(d['status']) == 'finished':
        statu.set("Completed")
        sbar.update()
        tmsg.showinfo("Message", "Video downloaded successfully")
    if(d['status']) == 'downloading':
        statu.set(f"{d['_percent_str']} of {d['_total_bytes_str']}  ")
        sbar.update()


def download_video():
    youtubelink = video_link.get()
    download_folder = directory.get()
    os.chdir(download_folder)
    try:
        statu.set("Downloading Started")
        sbar.update()
        ydl_opts = {
            'outtmpl': "/%(title)s.%(ext)s",
            'progress_hooks': [my_hook]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(youtubelink, download=True)

    except Exception as e:
        statu.set(e)
        sbar.update()
        tmsg.showinfo("Message",
                      "Found error in downloading video")


def Widgets():
    frame1 = Frame(root, bg="#000000")
    Label(frame1, text="Video Link", font="Arial 12 bold",
          padx=5, pady=7).grid(row=0, column=0, padx=10, pady=10)
    Label(frame1, text="Directory", font="Arial 12 bold",
          padx=9, pady=7).grid(row=1, column=0, padx=10, pady=10)
    frame1.pack(padx=15, pady=15, fill=X)

    Entry(frame1, textvariable=video_link, width=50, font="Arial 12", borderwidth=7,
          relief=FLAT).grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    Entry(frame1, textvariable=directory, width=33,  font="Arial 12",
          borderwidth=7, relief=FLAT).grid(row=1, column=1, padx=5, pady=5)

    browse = Button(frame1, text="Browse", command=browserdir,
                    width=15, font="Arial 12", bg="#05E8E0", pady=2)
    browse.grid(row=1, column=2, padx=1)

    download = Button(root, text="Download", command=download_video,
                      width=25, font="Arial 12", bg="#05E8E0",)
    download.pack(padx=1, pady=1)


root = Tk()
root.geometry("600x320")
root.title("Youtube Video Downloader")
root.config(background="#000000")
root.resizable(False, False)
statu = StringVar()
video_link = StringVar()
directory = StringVar()
Widgets()
statu.set("Start downloading")

sbar = Label(root, textvariable=statu, relief=SUNKEN, anchor=W, padx=4)
sbar.pack(side=BOTTOM, fill=X)
root.mainloop()
