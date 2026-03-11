import customtkinter as ctk
from datetime import date
from plyer import notification
from controle_de_validade import vencidinho, salvar


ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Sistema de Validade Lapa PR")
app.geometry("500x850")


def mostrar_alerta():
    hoje = date.today()
    alerta_encontrado = False


    for produto in vencidinho:
        data_venc = date(produto["ano do vencimento"],
                        produto["mes do vencimento"],
                        produto["dia do vencimento"])
        diferenca = (data_venc - hoje).days
        nome = produto["nome do produto"]


        if 0 <= diferenca <= 7:
            alerta_encontrado = True

            notification.notify(
                title="ALERTA DE VALIDADE",
                message=f"O produto {nome} venceu em {diferenca} dias!",
                timeout=10
        )
    if not alerta_encontrado:
        label_status.configure(text="Tudo em dia no estoque!", text_color="cyan")
    else:
        label_status.configure(text="Alerta enviados ao Windows!", text_color="orange")



def cadastrar_pela_interface():
    nome = entry_nome.get()
    data_texto = entry_data.get()
    qtd = entry_qtd.get()

    if nome == "" or data_texto == "" or qtd == "":
        label_status.configure(text="Erro: Preencha todos os campos!", text_color="red")
        return

    try:
        dia, mes, ano = map(int, data_texto.split("/"))

        novo_produto = {
            "nome do produto": nome.title(),
            "dia do vencimento": dia,
            "mes do vencimento": mes,
            "ano do vencimento": ano,
            "quantidade": int(qtd)
        }

        vencidinho.append(novo_produto)
        salvar()
        atualizar_lista()

        label_status.configure(text=f"✅ {nome} cadastrado com sucesso", text_color="green")

        entry_nome.delete(0, 'end')
        entry_data.delete(0, 'end')
        entry_qtd.delete(0, 'end')
        
    except:
        label_status.configure(text="Erro: Data deve ser DD/MM/AAAA", text_color="red")


def remover_item(nome_para_remover):
    global vencidinho
    vencidinho = [p for p in vencidinho if p["nome do produto"] != nome_para_remover]


    salvar()


    atualizar_lista()
    label_status.configure(text=f"{nome_para_remover} removido do estoque", text_color="yellow")


def atualizar_lista(filtro=""):
    for widget in frame_lista.winfo_children():
        widget.destroy()
    

    for produto in vencidinho:
        nome = produto["nome do produto"]


        if filtro.lower() in nome.lower():
            linha = ctk.CTkFrame(frame_lista, fg_color="transparent")
            linha.pack(fill="x", pady=2)


            data_venc = f"{produto['dia do vencimento']}/{produto['mes do vencimento']}/{produto['ano do vencimento']}"
            texto_exibir = f"{nome.ljust(15)}| {data_venc} | Qtd: {produto['quantidade']}"


            ctk.CTkLabel(linha, text=texto_exibir, font=("Courier", 11)).pack(side="left", padx=10)


            ctk.CTkButton(linha, text="x", width=30, height=20, fg_color="#aa0000",
                        hover_color="#880000",
                        command=lambda n=nome: remover_item(n)).pack(side="right", padx=10)

def buscar_produto(event):
    texto = entry_busca.get()
    atualizar_lista(texto)


titulo = ctk.CTkLabel(app, text="CADASTRO DE VALIDADE", font=("Roboto", 20, "bold"))
titulo.pack(pady=20)

entry_nome = ctk.CTkEntry(app, placeholder_text="Nome do Produto (Ex: Iogurte)", width=300)
entry_nome.pack(pady=10)

entry_data = ctk.CTkEntry(app, placeholder_text="Validade (DD/MM/AAAA)", width=300)
entry_data.pack(pady=10)

entry_qtd = ctk.CTkEntry(app, placeholder_text="Quantidade em estoque", width=300)
entry_qtd.pack(pady=10)

btn_salvar = ctk.CTkButton(app, text="CADASTRAR PRODUTO", command=cadastrar_pela_interface, fg_color="green", hover_color="darkgreen")
btn_salvar.pack(pady=20)

btn_alerta = ctk.CTkButton(app, text="VERIFCAR VENCIMENTOS", command=mostrar_alerta, fg_color="#D4A017", hover_color="#B8860B", font=("Roboto", 14, "bold"))
btn_alerta.pack(pady=10)

titulo_lista = ctk.CTkLabel(app, text="PRODUTOS EM ESTOQUE", font=("Roboto", 16, "bold"))
titulo_lista.pack(pady=(20, 5))

entry_busca = ctk.CTkEntry(app, placeholder_text="Pesquisar Produto...", width=300)
entry_busca.pack(pady=5)
entry_busca.bind("<KeyRelease>", buscar_produto)

frame_lista = ctk.CTkScrollableFrame(app,width=400, height=200)
frame_lista.pack(pady=10)

label_status = ctk.CTkLabel(app, text="")
label_status.pack(pady=10)

atualizar_lista()

app.mainloop()
