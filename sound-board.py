#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from pygame import mixer
import settings
import os

# the GUI main class
class GUI(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        settings.init()
        mixer.init()

        width, height, x, y = settings.center(master, 'master', 525, 355)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.master.configure(background='#333333')
        self.master.title("Compression Tool")
        img = tk.Image("photo", file=settings.ICON)
        self.tk.call('wm','iconphoto',root._w,img)
        self.browse_files = {}
        self.sound = {}
        self.item_id = {}
        # causes the full width of the window to be used
        self.columnconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)

        self.make_UI()

    # Generate the UI and set some global styles
    def make_UI(self):
        style = ttk.Style()
        # global style changes
        style.configure(".", background='#333333', foreground='orange', anchor="center")
        style.map("TButton", background=[('hover', '#222222')])
        style.map("TMenubutton", background=[('hover', '#222222')])
        style.map("TEntry", foreground=[('focus', 'blue2'), ('active', 'green2')])
        style.map("TCheckbutton", background=[('hover', '#222222')])

        heading = ttk.Label(self, text="Sound Board", font=("Courier", 20))
        heading.grid(column=0, row=1, rowspan=1, columnspan=3, sticky='NWES')
        col = 0
        row = 3
        i = 0
        self.grid_rowconfigure(3, minsize=100)
        for root, dirs, files in os.walk('sounds'):
            for clip in files:
                self.grid_rowconfigure(row, minsize=100)
                self.sound[i] = clip
                title = os.path.splitext(clip)[0]
                if len(title) > 10:
                    title = title[:15] + '\n' + title[15:]
                self.browse_files[i] = ttk.Button(self, text=title, command=lambda clip=clip: self.play(clip), state='active')
                self.browse_files[i].grid(column=col, row=row, rowspan=1, columnspan=1, sticky='WENS', padx=5, pady=5)
                i += 1
                col += 1
                if col >= 4:
                    col = 0
                    row += 1

    def play(self, clip):
        mixer.music.stop()
        mixer.music.load(os.getcwd() + "/sounds/" + clip)
        mixer.music.play()

    # exit the program
    def exit(self):
        quit()

if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root)
    window.pack(fill=tk.X, expand=True, anchor=tk.N)
    root.mainloop()