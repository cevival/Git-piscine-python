import tkinter as tk

def ajoutNageur():
    """Ajoute une personne qui réalise une nage pendant un certain nombre de longueurs"""
    a = entry_nom.get()
    b = entry_nage.get()
    c = entry_longueur.get()
    liste.append((a, b, c))
    entry_nom.delete(0, tk.END)
    entry_nage.delete(0, tk.END)
    entry_longueur.delete(0, tk.END)

def listeNageurs():
    """Liste toutes les performances de tous les nageurs"""
    output_text.delete(1.0, tk.END)
    for elt in liste:
        output_text.insert(tk.END, f"Prénom {elt[0]}, nage {elt[1]}, longueur {elt[2]}\n")

# Autres fonctions similaires pour les actions restantes...

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion de la piscine")

# Liste pour stocker les données
liste = []

# Widgets pour saisir les informations
label_nom = tk.Label(root, text="Qui nage ?")
entry_nom = tk.Entry(root)
label_nom.pack()
entry_nom.pack()

label_nage = tk.Label(root, text="Quelle nage ?")
entry_nage = tk.Entry(root)
label_nage.pack()
entry_nage.pack()

label_longueur = tk.Label(root, text="Combien de longueurs ?")
entry_longueur = tk.Entry(root)
label_longueur.pack()
entry_longueur.pack()

# Boutons pour les différentes actions
button_ajout = tk.Button(root, text="Ajouter nageur", command=ajoutNageur)
button_ajout.pack()

button_liste = tk.Button(root, text="Lister nageurs", command=listeNageurs)
button_liste.pack()

# Zone de texte pour afficher les résultats
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()