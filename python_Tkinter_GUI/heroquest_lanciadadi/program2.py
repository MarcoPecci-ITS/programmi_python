import tkinter as tk
import random

class DiceRoller:
    def __init__(self, master):
        self.master = master
        master.title("HEROQUEST - LANCIADADI")
        master.configure(bg='antiquewhite')
        master.update_idletasks()
        x = (master.winfo_screenwidth() - master.winfo_width()) // 2
        y = (master.winfo_screenheight() - master.winfo_height()) // 2
        master.geometry(f"+{x}+{y}")

        # Set row and column weights for center alignment and resizing
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Insert image
        self.image = tk.PhotoImage(file="hqlogosmall.png")
        self.label = tk.Label(master, image=self.image, bg='antiquewhite')
        self.label.grid(row=0, column=0, pady=10, columnspan=3)

        # Type of dice selection
        self.label2 = tk.Label(master, text="Scegli il tipo di dado:", font=("Century Schoolbook", 25))
        self.label2.grid(row=1, column=0, padx=20, sticky="n")
        self.dice_type = tk.StringVar(master, "Movimento")
        self.option_menu = tk.OptionMenu(master, self.dice_type, "Movimento", "Combattimento")
        self.option_menu.config(font=("Century Schoolbook", 22))
        self.option_menu.grid(row=1, column=1, columnspan=2, sticky="w")

        # Number of dice selection
        self.label3 = tk.Label(master, text="Scegli il numero di dadi:", font=("Century Schoolbook", 25))
        self.label3.grid(row=2, column=0, padx=20, sticky="n")
        self.dice_number = tk.StringVar(master, "2")
        options = [str(i) for i in range(1, 11)]
        self.option_menu2 = tk.OptionMenu(master, self.dice_number, *options)
        self.option_menu2.config(font=("Century Schoolbook", 22))
        self.option_menu2.grid(row=2, column=1, columnspan=2, sticky="w")

        # Roll button
        self.roll_button = tk.Button(master, text="Lancia dadi!", font=("Century Schoolbook", 25), command=self.roll_dice)
        self.roll_button.grid(row=3, column=0, columnspan=3)

        # Result display frame
        self.result_frame = tk.Frame(master)
        self.result_frame.grid(row=4, column=0, pady=20, columnspan=3)

        # Set row weight for result_frame to allow vertical centering
        master.grid_rowconfigure(4, weight=1)

    def roll_dice(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        dice_type = self.dice_type.get()
        dice_number = int(self.dice_number.get())

        if dice_type == "Combattimento":
            sides = {"Teschi": 3, "Scudi Eroi": 2, "Scudi Mostri": 1}
            result = [random.choice(list(sides.keys())) for _ in range(dice_number)]
            result_counts = {side: result.count(side) for side in sides}
            total_label_text = ", ".join([f"{result_counts[side]} {side}" for side in result_counts if result_counts[side] > 0])
            total_label = tk.Label(self.result_frame, text=total_label_text, font=("Arial", 25))
            total_label.pack()

        else:
            result = [random.randint(1, 6) for _ in range(dice_number)]
            result_string = ", ".join(map(str, result))
            total_label_text = f"{sum(result)} ({result_string})" if dice_number > 1 else str(sum(result))
            total_label = tk.Label(self.result_frame, text=total_label_text, font=("Arial", 30))
            total_label.pack()

root = tk.Tk()
my_gui = DiceRoller(root)
root.mainloop()