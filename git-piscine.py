import tkinter as tk
fenetre = tk.Tk()

fenetre.minsize(300,100)
fenetre.maxsize(300,100)

l = tk.Label(fenetre, text = "Que faut-il faire ?")
l.pack()
i = tk.Entry(fenetre, textvariable='string', width=30)
i.pack()
b = tk.Button(fenetre, text="Valider")
b.pack()
b = tk.Button(fenetre, text="Exit")
b.pack()
fenetre.mainloop()