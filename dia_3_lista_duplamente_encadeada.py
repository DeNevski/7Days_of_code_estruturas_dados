class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None
        self.anterior = None

class ListaDeProdutos:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Adiciona um produto na lista
    def adicionar(self, nome, codigo, preco, quantidade):
        novo_produto = Produto(nome, codigo, preco, quantidade)
        if self.head:
            novo_produto.anterior = self.tail
            self.tail.proximo = novo_produto
            self.tail = novo_produto            
        else:
            self.head = novo_produto
            self.tail = novo_produto

    # Remove um produto da lista
    def remover(self, codigo):
        if not self.head:
            raise ValueError('A lista está vazia!')
        elif self.head.codigo == codigo:
            self.head = self.head.proximo
            return True
        elif self.tail.codigo == codigo:
            self.tail = self.tail.anterior
            self.tail.proximo = None
            return True
        else:
            ponteiro = self.head.proximo
            while ponteiro:
                if ponteiro.codigo == codigo:
                    ponteiro.anterior.proximo = ponteiro.proximo
                    ponteiro.proximo.anterior = ponteiro.anterior
                    return True
                ponteiro = ponteiro.proximo
        raise IndexError('O código não foi encontrado!')
    
    # Mostra todos os produtos da lista
    def listar(self):
        ponteiro = self.head
        while ponteiro:
            print(f'Nome do produto: {ponteiro.nome:^15}  Código de barras: {ponteiro.codigo:^10}  Preço: R${ponteiro.preco:^10}  Quantidade: {ponteiro.quantidade:^10}')
            ponteiro = ponteiro.proximo
        print('='*110)

    # Altera a quantidade de um produto na lista
    def alterar(self, codigo, nova_qtd):
        if not isinstance(nova_qtd, int):
            raise ValueError(f'O valor {nova_qtd} é inválido!')
        
        if self.head.codigo == codigo:
            self.head.quantidade = nova_qtd
            return True
        elif self.tail.codigo == codigo:
            self.tail.quantidade = nova_qtd
            return True
        else:
            ponteiro = self.head.proximo
            while ponteiro:
                if ponteiro.codigo == codigo:
                    ponteiro.quantidade = nova_qtd
                    return True
                ponteiro = ponteiro.proximo
        raise IndexError('O código não foi encontrado!')    



lista = ListaDeProdutos()
lista.adicionar('Chocolate', 300, 7.00, 3)
lista.adicionar('Queijo', 400, 30.50, 5)
lista.adicionar('Sabão em pó', 500, 11.00, 1)
lista.adicionar('Carne', 600, 42.00, 7)
lista.listar()

lista.remover(500)
lista.listar()

lista.alterar(300, 10)
lista.listar()
