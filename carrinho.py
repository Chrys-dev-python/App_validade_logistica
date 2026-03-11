from datetime import datetime

nota = []
total = []
data = datetime.now()
data_hora = data.strftime("Data: %d/%m/%y Hora: %H:%M")


class Carrinho:
    def __init__(self, nome, preco, quantidade, preco_final):
        try:
            self.nome = nome
            self.preco = preco
            self.quantidade = quantidade
            self.preco_final = preco_final
        except ValueError:
            print("Valor ou Quantidade Incorrtos!")

        if quantidade > 1:
            self.preco_final = preco * quantidade
        else:
            self.preco_final = preco
        total.append(self.preco_final)
    



print("Nova compra")
escolha = input("realizar nova compra? ").lower()
if escolha == "sim":
    while True:
        nome_item = input("Qual o nome do produto? ")
        if nome_item.lower() == "sair":
            for i in nota:
                print(f"{i.nome} | Qtd: {i.quantidade} | preco R$:{i.preco:.2f} | Total R$:{i.preco_final:.2f}")
            subtotal = sum(total)
            
            if subtotal > 100.00:
                    resultado = subtotal * 10 / 100
                    subtotal = subtotal - resultado
                    print("desconto de 10% aplicado!")
                    print(subtotal)
                    print(data_hora)
                    break
            elif subtotal <= 100.00:
                print(subtotal)
                print(data_hora)
            
        else:
            preco_item = float(input("Qual o valor do produto? "))
            quantidade_item = int(input("Quantas unidades? "))

            if quantidade_item > 1:
                preco_final = preco_item * quantidade_item
            else:
                preco_final = preco_item

            itens = Carrinho(nome_item, preco_item, quantidade_item, preco_final)

            nota.append(itens)


