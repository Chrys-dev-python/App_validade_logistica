from datetime import date
import json
import os


def carregar_dados():
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []
    
vencidinho = carregar_dados()
            


def validade():

    while True:
        try:
            nome_produto = input("Qual o nome do produto? ").strip().title()
            dia_validade = int(input("Qual o dia de vencimento? "))
            mes_validade = int(input("qual o mes de vencimento? "))
            ano_validade = int(input("Qual o ano de vencimento? "))
            quantidade = int(input("Quantas unidades há deste produto? "))
            break
        except ValueError:
            print("caracters invalidos, por favor tente novamente!")
    
    cadastro_validade = {
        "nome do produto": nome_produto,
        "dia do vencimento": dia_validade,
        "mes do vencimento": mes_validade,
        "ano do vencimento": ano_validade,
        "quantidade": quantidade
    }

        

    vencidinho.append(cadastro_validade)
    salvar()
    print("produto salvo no arquivo!")


def salvar():
    with open("estoque.json", "w", encoding="utf-8") as f:
        json.dump(vencidinho, f, indent=4, ensure_ascii=False)



def data_alerta():
    hoje = date.today()

    print("--- Alerta, produto com praso curto! ---")
    for produto in vencidinho:
        data_validade = date(
            produto["ano do vencimento"],
            produto["mes do vencimento"],
            produto["dia do vencimento"]
        )

        diferenca = (data_validade - hoje).days
        nome = produto["nome do produto"]

        if diferenca < 0:
            print(f"Produto{nome} vencido a {abs(diferenca)} dias, retirar das prateleiras!")
        elif 0 <= diferenca <= 7:
            print(f"Alerta, produto {nome} esta a {diferenca} dias de vencer.")
        else:
            print(f"Produto {nome} esta em dia. Vence em {diferenca} dias.")

if __name__=="__main__":
    while True:
        opcoes = ("cadastrar", "alerta", "sair")
        print(opcoes)
        i = input("escolha uma das opções: ").lower().strip()

        if i == "cadastrar":
            validade()
        elif i == "alerta":
            data_alerta()
        elif i == "sair":
            break
        else:
            print("opção invalida!")
            break



