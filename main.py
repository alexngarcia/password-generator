import string
import random
from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()

        window_width = 400
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_pos_x = (screen_width / 2) - (window_width / 2)
        window_pos_y = (screen_height / 2) - (window_height / 2)

        self.geometry('%dx%d+%d+%d' % (window_width, window_height, window_pos_x, window_pos_y))
        self.resizable(False, False)
        self.title("Password Generator")
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    def close(self):
        msg = messagebox.askyesno("Exit", "Are you sure you want to close the program?")
        if msg is True:
            self.destroy()

    def create_widgets(self):

        def generate():
            size = int(pw_size.get()) if pw_size.get().isnumeric() else 8
            string_group = string.ascii_letters + string.digits + string.punctuation
            password.set(''.join(random.sample(string_group, size)))

        password = StringVar()
        pw_show = Entry(self, textvariable=password, font=('Helvetica', 20), justify='center')
        pw_show.grid(row=0, column=0, sticky=EW, columnspan=3, padx=20, pady=20)
        password.set("G3nAP4ssw0rd!")

        label = Label(self, text="Password length:", font=20)
        label.grid(row=1, column=0, padx=20, sticky=E)

        pw_size = Entry(self, font=20, width=5)
        pw_size.grid(row=1, column=1, padx=20, sticky=W)

        help_input = Label(self, text="If you don't input a number, the default size is 8.", font=('Helvetica', 8))
        help_input.grid(row=2, column=0, padx=20, columnspan=3, sticky=EW)

        button = Button(self, text="Generate!", font=15, relief=RIDGE, command=generate)
        button.grid(row=3, column=0, sticky=EW, columnspan=3, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
