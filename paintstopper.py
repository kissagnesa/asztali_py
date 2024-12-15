import tkinter as tk
import time

class StopperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopper")

        self.start_time = None  
        self.running = False    
        self.elapsed_time = 0   

        self.label = tk.Label(text="00:00:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Indít", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(self.root, text="Leállít", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self.root, text="Visszaállít", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        self.update_clock() 
        self.root.mainloop()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_clock()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.configure(text="00:00:00")

    def update_clock(self):
        if self.running:
            current_time = time.time() - self.start_time
            self.display_time(current_time)
        else:
            self.display_time(self.elapsed_time)
        self.root.after(100, self.update_clock)

    def display_time(self, total_seconds):
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        self.label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

app = StopperApp()
