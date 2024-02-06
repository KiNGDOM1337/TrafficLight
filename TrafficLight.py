import tkinter as tk
from time import sleep

class TrafficLightControl:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ampelschaltung")
        self.window.geometry("400x600")
        self.window.config(bg="#202020")

        self.navbar = tk.Label(self.window, height=2, bg="#202020")
        self.navbar.pack()

        self.canvas = tk.Canvas(self.window, width=200, height=400, bg="black") 
        self.canvas.pack(padx=0, pady=0)

        self.red = self.canvas.create_oval(50, 30, 150, 130, fill="#800000")
        self.yellow = self.canvas.create_oval(50, 150, 150, 250, fill="#808000")
        self.green = self.canvas.create_oval(50, 270, 150, 370, fill="#006000")

        btnStart = tk.Button(self.window, text="Start", command=self.run, width=15, height=2, font=('Arial', 12, "bold"), bg="#00c800", activebackground="#004000", borderwidth=3)
        btnStart.pack(side="left", padx=20)
        btnStop = tk.Button(self.window, text="Stop", command=self.reset, width=15, height=2, font=('Arial', 12, "bold"), bg="#c80000", activebackground="#400000", borderwidth=3) 
        btnStop.pack(side="right", padx=20)

        self.idle = True

        self.window.mainloop()

    def idle(self):
        if(self.idle == True):
            self.canvas.itemconfig(self.red, fill="#800000")
            self.canvas.itemconfig(self.yellow, fill="#808000")
            self.canvas.itemconfig(self.green, fill="#006000")

    def greenPhase(self):
        if(self.idle == False):
            self.canvas.itemconfig(self.red, fill="#800000")
            self.canvas.itemconfig(self.yellow, fill="#808000")
            self.canvas.itemconfig(self.green, fill="#00ff00")
            self.canvas.after(5000, self.yellowPhase)

    def yellowPhase(self):
        if(self.idle == False):
            self.canvas.itemconfig(self.red, fill="#800000")
            self.canvas.itemconfig(self.yellow, fill="#ffff00")
            self.canvas.itemconfig(self.green, fill="#006000")
            self.canvas.after(3000, self.redPhase)

    def redPhase(self):
        if(self.idle == False):
            self.canvas.itemconfig(self.red, fill="#ff0000")
            self.canvas.itemconfig(self.yellow, fill="#808000")
            self.canvas.itemconfig(self.green, fill="#006000")
            self.canvas.after(5000, self.redYellowPhase)
    
    def redYellowPhase(self):
        if(self.idle == False):
            self.canvas.itemconfig(self.red, fill="#ff0000")
            self.canvas.itemconfig(self.yellow, fill="#ffff00")
            self.canvas.itemconfig(self.green, fill="#006000")
            self.canvas.after(1000, self.run)

    def run(self):
        self.idle = False
        self.greenPhase()

    def reset(self):
        self.idle = True
        self.canvas.itemconfig(self.red, fill="#800000")
        self.canvas.itemconfig(self.yellow, fill="#808000")
        self.canvas.itemconfig(self.green, fill="#006000")


TrafficLightControl()