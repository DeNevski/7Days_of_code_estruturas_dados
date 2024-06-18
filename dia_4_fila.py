class Pedido:
    def __init__(self, nome_prato, mesa, valor):
        self.nome_prato = nome_prato
        self.mesa = mesa
        self.valor = valor
        self.proximo = None

class FilaDePedidos:
    def __init__(self):
        self.comeco = None
        self.final = None

    # Adiciona um pedido no final da fila
    def adicionar_pedidos(self, nome_prato, mesa, valor):
        novo_pedido = Pedido(nome_prato, mesa, valor)
        if self.comeco is None:
            self.comeco = novo_pedido
        
        if self.final is None:
            self.final = novo_pedido
        else:
            self.final.proximo = novo_pedido
            self.final = novo_pedido

    # Remove um pedido do inicio da fila
    def remover_pedidos(self):
        if self.comeco:
            self.comeco = self.comeco.proximo
        else:
            raise IndexError('Você está sem pedidos na fila!')
        
    # Lista todos pedidos na fila
    def listar_pedidos(self):
        if self.comeco:
            ponteiro = self.comeco
            while ponteiro:
                print(f'Nome do prato: {ponteiro.nome_prato:^30} Número da mesa: {ponteiro.mesa:^5} Valor total: R${ponteiro.valor:^10}')
                ponteiro = ponteiro.proximo
            print('=' * 90)
        else:
            return 'Não há pedidos na fila.'




pedidos = FilaDePedidos()
pedidos.adicionar_pedidos('Lasanha', 2, 40)
pedidos.adicionar_pedidos('Strogonoff de frango', 30, 35.99)
pedidos.adicionar_pedidos('Bife à milanesa', 25, 49.99)
pedidos.listar_pedidos()

pedidos.remover_pedidos()
pedidos.remover_pedidos()
pedidos.listar_pedidos()

pedidos.adicionar_pedidos('Espaguete', 9, 25)
pedidos.adicionar_pedidos('Pizza', 56, 45.50)
pedidos.listar_pedidos()

pedidos.remover_pedidos()
pedidos.listar_pedidos()

pedidos.remover_pedidos()
pedidos.remover_pedidos()
pedidos.remover_pedidos()
