
import tkinter as tk

# charger le fichier JSON
utilisateur = {
    "2023-01-18 06:48:31": [
        100.0,
        "GBP",
        100.0,
        "GBP"
    ],
    "2023-01-18 06:48:34": [
        100.0,
        "GBP",
        100.0,
        "GBP"
    ]
}

# accéder à l'historique
historique = utilisateur['2023-01-18 06:48:31']

# création de la fenêtre
fenetre = tk.Tk()
listbox = tk.Listbox(fenetre)

# ajout de l'historique à la listbox
for event in historique:
    listbox.insert(tk.END, event)

listbox.pack()
fenetre.mainloop()