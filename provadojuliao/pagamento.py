class Pagamento:
    def __init__(self, pedido, metodo_pagamento):
        self.pedido = pedido
        self.metodo_pagamento = metodo_pagamento

    def __str__(self):
        return f"Pagamento do pedido {self.pedido} via {self.metodo_pagamento}"

