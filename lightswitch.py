import tkinter as tk
window = tk.Tk()
window.geometry('300x200')
window.resizable(False, False)
window.title('Lightswitch')

button = tk.Button(text='Click me', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

def toggle(self):
    if button.config('text')[-1] == 'ON':
        button.config(text = 'OFF')
        window.config(bg = 'BLACK')
        print("Power was turned OFF.")
    else:
        button.config(text = 'ON')
        window.config(bg = 'YELLOW')
        print("Power was turned ON")

button.bind('<Button-1>', toggle)

# schijf hier tussen je code

window.mainloop()