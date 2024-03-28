import tkinter as tk
import random

class DiceRoller:
    def __init__(self, master):
        self.master = master
        master.title("HEROQUEST - LANCIADADI")
        master.geometry("800x600")
        # colore di sfondo
        master.configure(bg = 'antiquewhite')
        
        # centra la finestra
        master.update_idletasks()
        x = (master.winfo_screenwidth() - master.winfo_width()) // 2
        y = (master.winfo_screenheight() - master.winfo_height()) // 2
        master.geometry(f"+{x}+{y}")
        
        # inserisci immagine
        self.image = tk.PhotoImage(file="hqlogosmall.png")
        self.label = tk.Label(master, image=self.image, bg = 'antiquewhite')
        self.label.pack(anchor="center", pady = 10)

        self.frame1 = tk.Frame(master)
        self.frame1.pack(anchor="center", pady=5)

        self.label2 = tk.Label(self.frame1, text="Scegli il tipo di dado:", font=("Century Schoolbook", 25))
        self.label2.pack(side="left", padx=20)

        self.dice_type = tk.StringVar(master)
        self.dice_type.set("Movimento")
        self.option_menu = tk.OptionMenu(self.frame1, self.dice_type, "Movimento", "Combattimento")
        self.option_menu.config(font=("Century Schoolbook", 25))
        self.option_menu.pack(side="left")

        self.frame2 = tk.Frame(master)
        self.frame2.pack(anchor="center", pady=20)

        self.label3 = tk.Label(self.frame2, text="Scegli il numero di dadi:", font=("Century Schoolbook", 25))
        self.label3.pack(side="left", padx=20)

        self.dice_number = tk.StringVar(master)
        self.dice_number.set("2")
        self.option_menu2 = tk.OptionMenu(self.frame2, self.dice_number, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.option_menu2.config(font=("Century Schoolbook", 25))
        self.option_menu2.pack(side="left")

        self.roll_button = tk.Button(master, text="Lancia dadi!", font=("Century Schoolbook", 25), command=self.roll_dice)
        self.roll_button.pack(anchor="center")

        self.result_frame = tk.Frame(master)
        self.result_frame.pack(anchor="center", pady = 20)


    def roll_dice(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        dice_type = self.dice_type.get()
        dice_number = int(self.dice_number.get())

        if dice_type == "Combattimento":
            sides = ["Teschi"] * 3 + ["Scudi Eroi"] * 2 + ["Scudi Mostri"]
            result = [random.choice(sides) for i in range(dice_number)]
            result_counts = {"Teschi": 0, "Scudi Eroi": 0, "Scudi Mostri": 0}
            for res in result:
                result_counts[res] += 1
            total_label_text = ""
            for res_type, res_count in result_counts.items():
                if res_count > 0:
                    if total_label_text != "":
                        total_label_text += ", "
                    total_label_text += f"{res_count} {res_type}"
            total_label = tk.Label(self.result_frame, text=total_label_text, font=("Arial", 25))
            total_label.pack()


        else:
            result = [random.randint(1, 6) for i in range(dice_number)]
            result_string = ", ".join([str(i) for i in result])
            if dice_number == 1:
                total_label_text = f"{sum(result)}"
            else:
                total_label_text = f"{sum(result)} ({result_string})"
            total_label = tk.Label(self.result_frame, text=total_label_text, font=("Arial", 30))
            total_label.pack()


root = tk.Tk()
my_gui = DiceRoller(root)
root.mainloop()