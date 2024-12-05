class Pedido:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos
        self.total = sum(produto.preco for produto in produtos)

    def __str__(self):
        produtos_list = ', '.join([produto.nome for produto in self.produtos])
        return f"para {self.cliente.nome}: {produtos_list}, Total: R${self.total:.2f}"
