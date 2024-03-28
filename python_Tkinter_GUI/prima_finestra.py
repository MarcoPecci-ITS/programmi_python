import tkinter as tk

root = tk.Tk()  # crea la finestra
    
root.geometry('600x500')
root.title('La Mia Finestra')

label = tk.Label(root, text = 'Hello World!', font = ('Arial', 18))
label.pack(pady = '30')  # inserisco la scritta nella finestra, pady = distanza dall'alto

textbox = tk.Text(root, font = ('Arial', 16), height = 3)
textbox.pack(padx = '20')

button = tk.Button(root, text = 'Click me!', font = ('Arial', 16))
button.pack(pady = '20')

root.mainloop()