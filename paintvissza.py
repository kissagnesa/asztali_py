import tkinter as tk
import time

class CountdownApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Visszaszámláló")

        self.remaining_time = 300  
        self.running = False

        self.label = tk.Label(text="05:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Indít", command=self.start_countdown)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(self.root, text="Leállít", command=self.stop_countdown)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.root, text="Visszaállít", command=self.reset_countdown)
        self.reset_button.pack(side="left", padx=10)

        self.update_display()
        self.root.mainloop()

    def start_countdown(self):
        if not self.running and self.remaining_time > 0:
            self.running = True
            self.update_timer()

    def stop_countdown(self):
        self.running = False

    def reset_countdown(self):
        self.running = False
        self.remaining_time = 300  
        self.update_display()

    def update_timer(self):
        if self.running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
            self.root.after(1000, self.update_timer)
        elif self.remaining_time == 0:
            self.running = False
            self.label.configure(text="Idő lejárt!", fg="red")

    def update_display(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.label.configure(text=f"{minutes:02}:{seconds:02}")

app = CountdownApp()
