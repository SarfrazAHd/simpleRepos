import os
from tkinter import *
import tkinter.messagebox
from pygame import mixer
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk

from mutagen.mp3 import MP3
import threading
import time


mixer.init()

root = tk.ThemedTk()

root.get_themes()
root.set_theme("winxpblue")
#radiance

root.title("Music Player")
root.geometry("600x430+0+0")
root.resizable(False, False)
root.iconbitmap(r'music-player.ico')

file = ttk.Label(root, text="MP3 Player", relief=GROOVE, font=("times new roman", 30, 'bold'))
file.place(x=180, y=10)

file_length = ttk.Label(root, text="Total length 00 : 00", relief=GROOVE, font=("times new roman", 15, 'bold'))
file_length.place(x=295, y=105)

current_time = ttk.Label(root, text="Current Time 00 : 00",relief=GROOVE, font=("times new roman", 12, 'bold'))
current_time.place(x=305, y=145)


songs = ttk.Label(root, text="Song List", font=("Times new roman", 18, 'bold '))
songs.place(x=40, y=78)
listbox = Listbox(root, width=31, height=13, font=('times new roman', 10, 'bold'))
listbox.place(x=40, y=111)




play_img = PhotoImage(file="play.png")
pause_img = PhotoImage(file="pause.png")
stop_img = PhotoImage(file="Stop.png")
speaker_img = PhotoImage(file="speaker.png")
mute_img = PhotoImage(file="Mute.png")


song_list = []
def Browse_file():
    global file_path
    file_path = filedialog.askopenfilename()

    add_to_list(file_path)


def add_to_list(f):
    index = 0
    f = os.path.basename(f)
    listbox.insert(index, f)
    song_list.insert(0, file_path)
    index += 1



menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)
subMenus = Menu(menubar, tearoff=0)
subMenuss = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=subMenu)
menubar.add_cascade(label="View", menu=subMenus)
menubar.add_cascade(label="Exit", menu=subMenuss)

subMenu.add_command(label="Open File", command=Browse_file)
subMenus.add_command(label="View", command=lambda: print("This is view section"))



def song_details(file):

    file_data = os.path.splitext(file)

    if file_data[1] == ".mp3":
        audio = MP3(file)
        length = audio.info.length

    else:
        a = mixer.Sound(file)
        length = a.get_length()


    mins, sec = divmod(length, 60)
    mins = round(mins)
    sec = round(sec)

    timeformat = '{:02d} : {:02d}'.format(mins, sec)

    file_length['text'] = "Total length  " + timeformat
    #start_counter(length)


    t1 = threading.Thread(target=start_counter, args=(length,))
    t1.start()





def start_counter(t):

    while t and mixer.music.get_busy():
        mins, sec = divmod(t, 60)
        mins = round(mins)
        sec = round(sec)
        currentFormat = '{:02d} : {:02d}'.format(mins, sec)

        current_time['text'] = "Current time " + currentFormat
        time.sleep(1)
        t -= 1




def Play():
    try:
        pause

    except NameError:
        try:

            Stop()
            time.sleep(1)
            selectd_song = listbox.curselection()
            selectd_song = int(selectd_song[0])
            play_it = song_list[selectd_song]

            mixer.music.load(play_it)
            mixer.music.play()

            statusBar['text'] = "Playing Music" + '  ' + os.path.basename(play_it)

            song_details(play_it)

        except NameError:
            tkinter.messagebox.showerror("File not Found", "Kindly Upload Audio File")

    else:
        mixer.music.unpause()
        statusBar['text'] = "Music Resumed"





def Pause():
    global pause
    pause = True
    mixer.music.pause()
    statusBar['text'] = "Music Paused"



def Stop():
    global stop

    mixer.music.stop()
    statusBar['text'] = "Music Stopped"


def volume(val):
    vol = float(val) / 10
    mixer.music.set_volume(vol)


mute = False


def Mute():
    global mute

    if mute:
        mixer.music.set_volume(0.5)
        scale.set(5)
        statusBar['text'] = "Playing Music" + '  ' + os.path.basename(file_path)
        mute = False
    else:
        mixer.music.set_volume(0)
        scale.set(0)
        statusBar['text'] = "Music Muted"
        mute = True

# Differrent buttons
play_btn = ttk.Button(root, image=play_img, command=Play)
play_btn.place(x=290, y=185)

pause_btn = ttk.Button(root, image=pause_img, command=Pause)
pause_btn.place(x=355, y=185)

stop_btn = ttk.Button(root, image=stop_img, command=Stop)
stop_btn.place(x=420, y=185)

add_song_btn = ttk.Button(root, text="Add song",  command=Browse_file)
add_song_btn.place(x=52, y=325)

def del_song():
    selectd_song = listbox.curselection()
    selectd_song = int(selectd_song[0])
    listbox.delete(selectd_song)
    song_list.pop(selectd_song)






del_song_btn = ttk.Button(root, text="Delete song",  command=del_song)
del_song_btn.place(x=148, y=325)


speaker = ttk.Button(root, image=speaker_img, command=Mute).place(x=305, y=265)

scale = ttk.Scale(root, from_=0, to=10, orient=HORIZONTAL,   command=volume)
scale.place(x=355, y=272)
scale.set(5)

statusBar = ttk.Label(root, font=('times new roman', 12, 'bold'), text="Welcome to Python-Music player", anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


def close_window():
    Stop()
    root.destroy()

subMenuss.add_command(label="Exit", command = close_window)
root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()
