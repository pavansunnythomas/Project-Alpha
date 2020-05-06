import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as msg
import os

window1 = tk.Tk()
HEIGHT = 600
WIDTH = 800
HOME = os.getcwd()
FILE = None
FILEPATH = tk.StringVar()
frames = list(
    map(lambda i: (tk.PhotoImage(file=HOME + f"/Assets/fire animation/frame_{i}_delay-0.04s.gif")), range(50)))


def browse():
    global FILE, FILEPATH
    file = fd.askopenfile(mode='r', title='select file', filetypes=[('all files', '*.*')])
    if file is not None:
        app.entry_bar.delete(0, len(FILEPATH.get()))
        app.entry_bar.insert(0, file.name)
        FILE = file.read()


def upload():
    global FILE, FILEPATH
    if FILE:
        pass  # Use the APIs accordingly
        FILE = None
    elif FILEPATH.get():
        try:
            FILE = open(file=FILEPATH.get(), mode='r')
            pass
            FILE = None
        except:
            msg.showinfo(title='Invalid File', message='Please Upload a Valid File')
            browse()
    else:
        msg.showinfo(title='No File Found', message='Please Upload any File')


class Alpha(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, height=600, width=800, bg='black')
        self.master = master
        self.can = tk.Canvas(master=self, height=128, width=WIDTH, bg='black', highlightthickness=0)
        self.can.place(y=472, x=0)
        self.can.focus_set()
        self.pack()
        self.fire_animation()
        self.update()

    def label(self, text, x_cord, y_cord, size=12):
        tittle = tk.Label(master=self, text=text, font=('Times', str(size)))
        tittle.place(y=y_cord, x=x_cord)

    def entry(self, x_cord, y_cord, width=30, size=14):
        global FILEPATH
        self.entry_bar = tk.Entry(master=self, width=width, font=('Times', str(size)), textvariable=FILEPATH)
        self.entry_bar.place(y=y_cord, x=x_cord)

    def button(self, text, x_cord, y_cord, width=10, height=1, size=12, command=None):
        button = tk.Button(master=self, text=text, width=width, height=height, font=('Times', str(size)),
                           command=command)
        button.place(y=y_cord, x=x_cord)

    def folder_upload(self):
        self.label('File to upload :', 10, 250)
        self.entry(120, 250, width=74)  # for linux distros => 150, 250, width=79
        self.button('Browse', 280, 300, command=browse)
        self.button('Upload', 400, 300, command=upload)

    def updategif(self, increment, item):
        frame = frames[increment]
        increment += 1

        if increment >= 49:
            increment = 0

        self.can.itemconfig(item, image=frame)
        self.after(50, self.updategif, increment, item)

    def fire_animation(self):
        for i in range(WIDTH // 128 + 1):
            fire = self.can.create_image((128 * i, 0), image=frames[0])
            self.after(0, self.updategif, 0, fire)


# window1 properties
window1.geometry(f'{WIDTH}x{HEIGHT}')
window1.config(bg='black')
window1.resizable(width=False, height=False)
window1.title(string='Project Alpha v 0.0.0')

# App working
app = Alpha(master=window1)
app.label('Project Alpha', 310, 40, 20)
app.folder_upload()

# App initialisation
app.mainloop()
