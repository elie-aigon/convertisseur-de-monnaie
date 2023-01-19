import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import json
from datetime import datetime


def main():

    # colors
    col1 = "#FFFFFF"  # blanc
    col3 = "#8B8E93"  # gris

    # je load tout mes json au debut pour avoir accès à mes listes et dictionnaires
    with open('currency.json', 'r') as f:
        currency = json.load(f)
    with open('favoris.json', 'r') as f:
        favoris = json.load(f)
    with open('table.json', 'r') as f:
        table = json.load(f)
    with open('hisory.json', 'r') as f:
        history = json.load(f)

    window = Tk()
    window.geometry('350x300')
    window.title('Convertisseur ')
    window.configure(bg=col1)
    window.resizable(height=False, width=False)

    # résultat
    resultatstr = tk.StringVar()

    result = tk.Label(window, state="normal", width=28, height=3, pady=7, bg=col1, relief=SOLID)
    result['textvariable'] = resultatstr
    result.place(x=50, y=10)

    # input devise
    from_label = Label(window, text='De:', compound=LEFT, width=8, height=1, pady=0, anchor=NW, bg=col1)
    from_label.place(x=48, y=90)
    combo1 = ttk.Combobox(window, values=favoris + currency, state='readonly', width=8, justify=CENTER)
    combo1.place(x=50, y=115)

    to_label = Label(window, text='à:', compound=LEFT, width=8, height=1, pady=0, anchor=NW, bg=col1)
    to_label.place(x=178, y=90)
    combo2 = ttk.Combobox(window, values=favoris + currency, state="readonly", width=8, justify=CENTER)
    combo2.place(x=180, y=115)

    value = Entry(window, width=33, justify=CENTER, relief=SOLID)
    value.place(x=50, y=155)

    # bouton
    button = Button(window, text='Convertisseur', width=26, padx=5, height=1, bg=col3, relief=SOLID)
    button.config(command=lambda: convertisseur())
    button.place(x=50, y=200)

    add_devise = Button(window, text='Ajouter une devise', width=26, padx=5, height=1, bg=col3, relief=SOLID)
    add_devise.config(command=lambda: add_devise_window())
    add_devise.place(x=50, y=250)

    history_button = Button(window, text='H', width=5, height=1, bg=col3, relief=SOLID)
    history_button.config(command=lambda: show_history())
    history_button.place(x=280, y=10)

    fav = Button(window, text='F', width=5, height=1, bg=col3, relief=SOLID)
    fav.config(command=lambda: fav_window_pop())
    fav.place(x=280, y=50)

    def fav_window_pop():  # affiche la fenetre d'ajout de favoris ainsi que sa liste

        fav_window = Tk()
        fav_window.title("Favoris")

        input_label = Label(fav_window, text="Entrez le code iso : ")
        input_label.place(x=30, y=20)

        input_fav = Entry(fav_window, )
        input_fav.place(x=32, y=40)

        listbox = Listbox(fav_window,  relief=SOLID)
        listbox.place(x=30, y=100)

        # bouton ajouter
        add_fav_button = Button(fav_window, text="Ajouter", bg=col3, height=1, width=10, relief=SOLID)
        add_fav_button.config(command=lambda: add_fav(input_fav))
        add_fav_button.place(x=55, y=70)

        for item in favoris:
            listbox.insert(END, item)

    def add_fav(input_fav):  # ajoute un élément à une liste de favoris
        fav_element = input_fav.get().upper()
        if fav_element not in favoris:
            favoris.append(fav_element)
            messagebox.showinfo("", "Cette monnaie a été ajouté aux favoris \n Vos favoris seront affichés aux début du menu déroulant du convertisseur.")
        else:
            messagebox.showinfo("", "Cette monnaie est déja dans les favoris")

        with open('favoris.json', 'w') as f:
            json.dump(favoris, f)
        return favoris

    def show_history():  # affiche l'historique
        hist_window = Tk()
        hist_window.geometry('330x200')
        hist_window.title("Historique")

        input_label = Label(hist_window, text="Historique : ")
        input_label.place(x=30, y=20)

        listbox = Listbox(hist_window, width=40, height=50, relief=SOLID)
        listbox.place(x=30, y=40)

        for key, value in history.items():
            listbox.insert(END, key, value)

    def convertisseur():

        heure = datetime.now()
        formated_time = heure.strftime("%Y-%m-%d %H:%M:%S")
        formated_time = str(formated_time)
        count = value.get()
        count = float(count)
        devise1 = combo1.get()
        devise2 = combo2.get()

        if count > 0:
            resultat_valeur = round(count * 1 / table[devise1] * table[devise2], 3)
            resultat = str(resultat_valeur) + ' ' + devise2
            resultatstr.set(resultat)

            history[formated_time] = [count, devise1, '=>', resultat_valeur, devise2]
            with open('hisory.json', 'w') as f:
                json.dump(history, f)
        else:
            pass

    def add_devise_window():
        # new window
        subwindow = Toplevel(window)
        subwindow.geometry('200x200')
        subwindow.title("Nouvelle dévise")
        # input

        value_new = Label(subwindow, text='Valeur: ', width=8, height=1, anchor=NW)
        value_new.place(x=38, y=60)
        new_devise_value = Entry(subwindow, width=8, justify=CENTER, bg=col1, relief=SOLID)

        new_devise_value.place(x=40, y=80)

        code_iso = Label(subwindow, text='Code iso: ', width=8, height=1)
        code_iso.place(x=113, y=60)
        new_devise_name = Entry(subwindow, width=8, justify=CENTER, bg=col1, relief=SOLID)

        new_devise_name.place(x=115, y=80)

        ok_button = Button(subwindow, text='OK', width=16, height=1, bg=col3, relief=SOLID)
        ok_button.config(command=lambda: add_devise(new_devise_name, new_devise_value))
        ok_button.place(x=42, y=120)

    def add_devise(new_devise_name, new_devise_value):
        devise_name = new_devise_name.get().upper()
        devise_value = float(new_devise_value.get())

        table[devise_name] = devise_value
        with open('table.json', 'w') as f:
            json.dump(table, f)

        currency.append(devise_name)
        with open('currency.json', 'w') as f:
            json.dump(currency, f)
        messagebox.showinfo("Information", "Votre nouvelle devise a été ajoutée")
        window.destroy()
        main()
    window.mainloop()


main()
