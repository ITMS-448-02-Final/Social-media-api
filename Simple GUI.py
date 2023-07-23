from tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="API Query Parser/Interpreter", fg='white', bg='grey', font=("Courier", 15))
        self.label.pack()
        self.master.geometry("500x270")
        


        self.Functionality_button1 = Button(master, text="API1", command=self.API1, height=2, width=490, fg='white', bg='black', font=("Courier", 15))
        self.Functionality_button1.pack()

        self.Functionality_button2 = Button(master, text="API2", command=self.API2, height=2, width=490,bg='white', fg='black', font=("Courier", 15))
        self.Functionality_button2.pack()



        self.greet_button = Button(master, text="Greet", command=self.greet, height=2, width=490, fg='white', bg='black', font=("Courier", 15))
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit, height=2, width=490,bg='white', fg='black', font=("Courier", 15))
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
