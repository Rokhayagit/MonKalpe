import tkinter as tk

def calculer_depenses():
    try:
        budget = float(entree_budget.get())
        logement = float(entree_logement.get())
        nourriture = float(entree_nourriture.get())
        transport = float(entree_transport.get())
        autres = float(entree_autres.get())
        total = logement + nourriture + transport + autres
        restant = round(budget - total, 2)
        label_resultat["text"] = f"Dépenses totales : {total} FCFA\nSolde restant : {restant} FCFA"
    except ValueError:
        label_resultat["text"] = "Valeur invalide"

fenetre = tk.Tk()
fenetre.title("Calculatrice de Dépenses")
fenetre.geometry("400x300")
fenetre.resizable(False, False)

tk.Label(fenetre, text="Budget (FCFA)").grid(row=0, column=0, sticky="w", pady=5)
entree_budget = tk.Entry(fenetre)
entree_budget.grid(row=0, column=1)

tk.Label(fenetre, text="Logement").grid(row=1, column=0, sticky="w", pady=5)
entree_logement = tk.Entry(fenetre)
entree_logement.grid(row=1, column=1)

tk.Label(fenetre, text="Nourriture").grid(row=2, column=0, sticky="w", pady=5)
entree_nourriture = tk.Entry(fenetre)
entree_nourriture.grid(row=2, column=1)

tk.Label(fenetre, text="Transport").grid(row=3, column=0, sticky="w", pady=5)
entree_transport = tk.Entry(fenetre)
entree_transport.grid(row=3, column=1)

tk.Label(fenetre, text="Autres").grid(row=4, column=0, sticky="w", pady=5)
entree_autres = tk.Entry(fenetre)
entree_autres.grid(row=4, column=1)

bouton_calculer = tk.Button(fenetre, text="Calculer", command=calculer_depenses)
bouton_calculer.grid(row=5, column=0, columnspan=2, pady=10)

label_resultat = tk.Label(fenetre, text="", fg="blue")
label_resultat.grid(row=6, column=0, columnspan=2)

fenetre.mainloop()
