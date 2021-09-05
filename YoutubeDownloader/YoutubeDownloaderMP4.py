#https://python-forum.io/Thread-Display-image-from-URL
#https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-windows-clipboard-from-python

from tkinter import Tk, Label, Button, Entry, Canvas, messagebox, filedialog
import pytube
from PIL import ImageTk, Image
from io import BytesIO
import urllib
import urllib.request
import win32clipboard


youtube = ""
raw_data = ""
url = ""
video = ""

class DOWNLOADER:
    def __init__(self, master):
        self.master = master
        master.title("YouTube downloader")

def searchURL():
    global url, raw_data
    
    url = entry1.get()
    try:
        global youtube
        youtube = pytube.YouTube(url)
        #print(":" + youtube.thumbnail_url)

        Title.config(text=youtube.title)

        with urllib.request.urlopen(youtube.thumbnail_url) as u: #pytube.YouTube("https://www.youtube.com/watch?v=b-Y01c1LsOM")
            raw_data = u.read()
        im = Image.open(BytesIO(raw_data)) #BytesIO(raw_data)
        im = im.resize((300,250), Image.ANTIALIAS) #w, h
        global image
        image = ImageTk.PhotoImage(im)
        label = Label(image=image)
        canvas1.create_window(200, 275, window=label)

        canvas1.update()

        button2 = Button(text='Download', command=download, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(200, 425, window=button2)

        canvas1.update_idletasks()

    except pytube.exceptions.RegexMatchError:
        messagebox.showinfo("Error", "This video doesn't exist.")

def download():
    #messagebox.showinfo("Download","Downloaded in same folder as program")
    folder_selected = filedialog.askdirectory() 
    video = youtube.streams.first()
    video.download(folder_selected)
    
def pasteTEXT(self):
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print(data)

root = Tk()

canvas1 = Canvas(root, width = 400, height = 425,  relief = 'raised')
canvas1.pack()

label1 = Label(root, text='Youtube Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

entry1 = Entry(root, width = 50)
entry1.bind("<Control-v>", pasteTEXT)
canvas1.create_window(200, 50, window=entry1)

button1 = Button(text='Search', command=searchURL, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 75, window=button1)

Title = Label(root)
Title.config(font=('helvetica', 11))
canvas1.create_window(200, 125, window=Title)

#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
#youtube = pytube.YouTube(url)
#print(youtube.thumbnail_url)

#Title = Label(root, text=youtube.title)
#Title.config(font=('helvetica', 11))
#canvas1.create_window(200, 125, window=Title)

"""with urllib.request.urlopen(pytube.YouTube("https://www.youtube.com/watch?v=b-Y01c1LsOM").thumbnail_url) as u:
    raw_data = u.read()
im = Image.open(BytesIO(raw_data))
im = im.resize((300,250), Image.ANTIALIAS) #w, h
image = ImageTk.PhotoImage(im)
label = Label(image=image)
canvas1.create_window(200, 275, window=label)"""

"""button2 = Button(text='Download', command=searchURL, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 425, window=button2)"""

root.geometry("500x450") #width x height
my_gui = DOWNLOADER(root)

root.mainloop()