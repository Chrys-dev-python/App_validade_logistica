import customtkinter as ctk
from controle_de_validade import carregar_dados, salvar, vencidinho


app = ctk.CTk()
app.title("controle de validade - Lapa PR")
app.geometry("400x300")


def btn_salvar_clique():
    salvar()
    print("dados salvos via Interface")


btn = ctk.CTkButton(app, text="Salvar Estoque", command=btn_salvar_clique)
btn.pack(pady=20)


app.mainloop()