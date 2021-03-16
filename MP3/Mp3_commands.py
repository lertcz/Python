#import Mp3Player
from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
from mutagen.mp3 import MP3
import pygame
import time
import os
import sqlite3
from sqlite3 import Error
from PIL import Image, ImageTk

database = r"Songs.db"
pygame.mixer.init()

global conn, cursor

#connect to database
conn = sqlite3.connect(database)
cursor = conn.cursor()

def initList():
    cursor.execute("SELECT * FROM Songs")
    table = cursor.fetchall()
    for row in table:
        song_box.insert(END, row[1])
    conn.commit()

def create_table():

    sql ='''CREATE TABLE IF NOT EXISTS Songs (
        PATH CHAR(50),
        NAME CHAR(30)
        ); '''
    cursor.execute(sql)
    conn.commit()

def add_Song_table():

    sql ='''CREATE TABLE IF NOT EXISTS Songs (
        PATH text,
        NAME text
        ); '''
    cursor.execute(sql)
    conn.commit()

def on_closing(root):
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #deleteall(conn, cursor)
    conn.close()   
    root.destroy()

def add_songs():
    songs = filedialog.askopenfilenames(initialdir="audio", title="Chose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        whole = song
        song = song.replace(".mp3", "")
        song = song[song.rindex("/")+1:]

        cursor.execute("SELECT * FROM Songs where PATH=?", (whole, ))
        if(cursor.fetchone() == None):
            cursor.execute("INSERT INTO Songs VALUES(?, ?)", (whole, song))

    song_box.delete(0, END)

    cursor.execute("SELECT * FROM Songs")
    table = cursor.fetchall()
    for row in table:
        song_box.insert(END, row[1])
    conn.commit()

def mp3gen(folder):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

def add_song_folder():
    folder = filedialog.askdirectory(initialdir="audio", title="Chose a song file")

    for song in mp3gen(folder):
        whole = song
        song = song.replace(".mp3", "")
        song = song[song.rindex("/")+1:]
        song = song[song.rindex("\\")+1:]
        #print(song)

        cursor.execute("SELECT * FROM Songs where PATH=?", (whole, ))
        if(cursor.fetchone() == None):
            cursor.execute("INSERT INTO Songs VALUES(?, ?)", (whole, song))
        
        song_box.delete(0, END)

        cursor.execute("SELECT * FROM Songs")
        table = cursor.fetchall()
        for row in table:
            song_box.insert(END, row[1])
        conn.commit()

def delete_song():
    cursor.execute("DELETE FROM Songs WHERE NAME=?", (song_box.get(ACTIVE), ))
    conn.commit()
    song_box.delete(0, END)

    cursor.execute("SELECT * FROM Songs")
    table = cursor.fetchall()
    for row in table:
        song_box.insert(END, row[1])
    conn.commit()

def delete_all_songs():
    cursor.execute("DELETE FROM Songs")
    conn.commit()
    song_box.delete(0, END)

    cursor.execute("SELECT * FROM Songs")
    table = cursor.fetchall()
    for row in table:
        song_box.insert(END, row[1])
    conn.commit()

def play(self, Path):
    global paused
    my_slider.config(value=0) 

    paused = FALSE
    play_btn.config(image=pause_btn_img)

    cursor.execute("Select * FROM Songs where NAME=?", (Path, ))
    song = cursor.fetchone()[0]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()

global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if(paused): #paused
        pygame.mixer.music.unpause()
        paused = False
        play_btn.config(image=pause_btn_img)
    else: #not paused
        pygame.mixer.music.pause()
        paused = True
        play_btn.config(image=play_btn_img)

def nextSong():
    if(song_box.curselection()[0]+1 == song_box.size()):
        my_slider.config(value=0) 

        #clear active song bar
        song_box.select_clear(0, END)
        #activate new song bar
        song_box.activate(0)
        #set active bar
        song_box.selection_set(0, last=None)
        song_box.see(song_box.curselection())
        
        cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ACTIVE), ))
        song = cursor.fetchone()[0]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    else:
        my_slider.config(value=0) 

        #get the next song
        next_one = song_box.curselection()[0]+1
        #clear active song bar
        song_box.select_clear(0, END)
        #activate new song bar
        song_box.activate(next_one)
        #set active bar
        song_box.selection_set(next_one, last=None)
        song_box.see(next_one)

        cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ACTIVE), ))
        song = cursor.fetchone()[0]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

def previousSong():
    next_one = song_box.curselection()[0]-1
    if(next_one == -1):
        my_slider.config(value=0) 

        song_box.select_clear(0, END)
        song_box.selection_set("end")
        song_box.activate("end")
        song_box.see("end")

        #load and play a song
        cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ACTIVE), ))
        song = cursor.fetchone()[0]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    else:
        my_slider.config(value=0) 

        #clear active song bar
        song_box.select_clear(0, END)
        #activate new song bar
        song_box.activate(next_one)
        #set active bar
        song_box.selection_set(next_one) #, last=None)
        song_box.see(next_one)
        #load and play a song
        cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ACTIVE), ))
        song = cursor.fetchone()[0]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

#create slide func
def slide(x):
    if(not paused):
        cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ANCHOR), ))
        song = cursor.fetchone()[0]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def play_time():
    global song_length
    
    #get current itme
    current_time = pygame.mixer.music.get_pos() / 1000
    #convert time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    cursor.execute("Select * FROM Songs where NAME=?", (song_box.get(ACTIVE), ))
    song = cursor.fetchone()[0]
    #get song lenght
    global song_length
    song_length = MP3(song).info.length

    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    current_time += 1
    if(int(my_slider.get()) == int(song_length)):
        #status_bar.config(text="Time Elapsed: " + converted_song_length + "  of  " + converted_song_length)
        label_current.config(text=converted_song_length)
        label_lenght.config(text=converted_song_length)
        nextSong()
    elif(paused):
        label_current.config(text=time.strftime('%M:%S', time.gmtime(int(my_slider.get()))))
        label_lenght.config(text=converted_song_length)
        pass
    elif(int(my_slider.get()) == int(current_time)):
        #update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        #slider has been moved
        #update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))

        #convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        
        #output time to status bar
        #status_bar.config(text="Time Elapsed: " + converted_current_time + "  of  " + converted_song_length)

        label_current.config(text=converted_current_time)
        label_lenght.config(text=converted_song_length)

        # move along by 1 second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
    
    label_current.after(1000, play_time)

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())



def window():
    global song_box, status_bar, my_slider, play_btn, play_btn_img, pause_btn_img, label_current, label_lenght, volume_slider

    root = Tk()
    root.title("MP3 Player")
    root.geometry("550x400")

    #create master frame
    master_frame = Frame(root)
    master_frame.pack(pady=20)

    #playlist box
    song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
    song_box.grid(row=0, column=1)

    #define player control buttons
    back_btn_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/graphic/back.png')#PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + '/graphic/back.png')
    back_btn_img = back_btn_img.resize((40, 40), Image.ANTIALIAS)
    back_btn_img = ImageTk.PhotoImage(back_btn_img)
    
    forward_btn_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/graphic/forward.png')#PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + '/graphic/forward.png')
    forward_btn_img = forward_btn_img.resize((40, 40), Image.ANTIALIAS)
    forward_btn_img = ImageTk.PhotoImage(forward_btn_img)
    
    play_btn_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/graphic/play.png')#PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + '/graphic/play.png')
    play_btn_img = play_btn_img.resize((40, 40), Image.ANTIALIAS)
    play_btn_img = ImageTk.PhotoImage(play_btn_img)
    
    pause_btn_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/graphic/pause.png') #PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + '/graphic/pause.png')
    pause_btn_img = pause_btn_img.resize((40, 40), Image.ANTIALIAS)
    pause_btn_img = ImageTk.PhotoImage(pause_btn_img)
    
    speaker_img = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/graphic/speaker.png')
    speaker_img = speaker_img.resize((20, 20), Image.ANTIALIAS)
    speaker_img = ImageTk.PhotoImage(speaker_img)

    #create player control frame
    controls_frame = Frame(master_frame)
    controls_frame.grid(row=1, column=1, pady=20)

    #create player control buttons
    back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previousSong)
    play_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
    forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=nextSong)

    back_btn.grid(row=0, column=0, padx=10)
    play_btn.grid(row=0, column=1, padx=10)
    forward_btn.grid(row=0, column=2, padx=10)

    #create player control frame
    controls_frame = Frame(master_frame)
    controls_frame.grid(row=1, column=0, pady=20)

    #create volume frame
    volume_frame = Frame(master_frame)
    volume_frame.grid(row=3, column=1, padx=20)

    #create menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    #add song menu
    add_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
    add_song_menu.add_command(label="Add songs", command=add_songs)
    add_song_menu.add_command(label="Pick song folder", command=add_song_folder)

    #add remove song menu
    remove_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)
    remove_song_menu.add_command(label="Delete song", command=delete_song)
    remove_song_menu.add_command(label="Delete all songs", command=delete_all_songs)

    #create status bar
    #status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
    #status_bar.pack(fill=X, side=BOTTOM, ipady=2)

    #create music positioner slider
    my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
    my_slider.grid(row=2, column=1, pady=20)

    label_current = Label(master_frame, text = '00:00')
    label_current.grid(row=2, column=0, pady=30, padx=10)

    label_lenght = Label(master_frame, text='00:00')
    label_lenght .grid(row=2, column=2, pady=30, padx=10)

    volume_img = Label(volume_frame, image=speaker_img)
    volume_img.grid(row=0, column=0, pady=10)
    volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=HORIZONTAL, value=1, command=volume, length=75)
    volume_slider.grid(row=0, column=1, pady=10)

    initList()

    song_box.bind('<Double-Button>', lambda x: play(x, song_box.get(ANCHOR)))
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()