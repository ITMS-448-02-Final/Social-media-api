from tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="A simple GUI!")
        self.label.pack()


        self.Functionality_button1 = Button(master, text="API1", command=self.API1)
        self.Functionality_button1.pack()

        self.Functionality_button2 = Button(master, text="API2", command=self.API2)
        self.Functionality_button2.pack()



        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")
    def API1(self):
        print("API1 results")
    def API2(self):
        print("API2 results")

root = Tk()
my_gui = GUI(root)
root.mainloop()
