from cliente import Cliente
from funcionario import Funcionario
from produto import Produto
from pedido import Pedido
from pagamento import Pagamento

# Criando alguns clientes, funcionários e produtos para teste
cliente1 = Cliente("Carlos", "carlindugrau@gmail.com", "123456789")
funcionario1 = Funcionario("Benê", "Atendente", 1500.00)
produto1 = Produto("Hamburger", 12.50)
produto2 = Produto("Suco", 3.00)

# Criando um pedido
pedido1 = Pedido(cliente1, [produto1, produto2])

# Registrando um pagamento
pagamento1 = Pagamento(pedido1, "Cartão de Crédito")

print(cliente1)
print(funcionario1)
print(produto1)
print(produto2)
print(pedido1)
print(pagamento1)
