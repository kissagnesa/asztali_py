import tkinter as tk
import random

class Labda:
    def __init__(self, x, y, xirany, yirany, meret, szin):
        self.x = x
        self.y = y
        self.xirany = xirany
        self.yirany = yirany
        self.meret = meret
        self.szin = szin  


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Labdák")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='lavender')
        self.canvas.pack()

        self.labdalista = []
        self.create_random_balls(17)

        self.update_clock()
        self.root.mainloop()

    def create_random_balls(self, ball_count):
        """Létrehozza a labdákat véletlenszerű paraméterekkel"""
        for _ in range(ball_count):
            x = random.randint(50, 750)  
            y = random.randint(50, 550)  
            xirany = random.choice([-4, -3, -2, 2, 3, 4])  
            yirany = random.choice([-4, -3, -2, 2, 3, 4])  
            meret = random.randint(10, 50)  
            szin = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])  
            self.labdalista.append(Labda(x, y, xirany, yirany, meret, szin))

    def update_clock(self):
        """Labdák mozgatása és kirajzolása"""
        self.canvas.delete("all")  
        for labda in self.labdalista:
            if labda.x + labda.meret > 800 or labda.x < 0:
                labda.xirany *= -1
            if labda.y + labda.meret > 600 or labda.y < 0:
                labda.yirany *= -1

            labda.x += labda.xirany
            labda.y += labda.yirany

            self.canvas.create_oval(
                labda.x, labda.y, 
                labda.x + labda.meret, labda.y + labda.meret, 
                fill=labda.szin, outline=""
            )

        self.root.after(20, self.update_clock)


app = App()
