class Node:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return f'\nID: {self.id:^5}  NOME: {self.nome:^10}  QUANTIDADE: {self.quantidade:^5}'

class ArvoreProduto:
    def __init__(self):
        self.raiz = None

    # Insere um novo nó na árvore e caso já exista um nó com o mesmo id, atualiza os valores "nome" e "quantidade"
    def inserir(self, id, nome, quantidade):
        pai = None
        node = self.raiz
        while node:
            pai = node
            if id == node.id:
                node.nome = nome
                node.quantidade = quantidade
                return False
            if id < node.id:
                node = node.esquerda
            else:
                node = node.direita

        if self.raiz is None:
            self.raiz = Node(id, nome, quantidade)
        elif id < pai.id:
            pai.esquerda = Node(id, nome, quantidade)
        elif id > pai.id:
            pai.direita = Node(id, nome, quantidade)

    # Busca por um id desejado e retorna o seu valor
    def buscar(self, id, node=None):
        try:
            if node is None:
                node = self.raiz
            if id == node.id:
                return node
            if id < node.id:
                return self.buscar(id, node.esquerda)
            elif id > node.id:
                return self.buscar(id, node.direita)
        except:
            print('ID não encontrado!')
        


arvore = ArvoreProduto()
arvore.inserir(56, 'Calça', 100)
arvore.inserir(2, 'Short', 500)
arvore.inserir(10, 'Camisa', 56)
arvore.inserir(2, 'Short', 88)
arvore.inserir(56, 'Calça', 258)
arvore.inserir(10, 'Camisa', 555)
arvore.inserir(100, 'Sapato', 888)
arvore.inserir(100, 'Tênis', 457)
arvore.inserir(1, 'Blusa de frio', 10)
arvore.inserir(1, 'Blusa de frio', 101)

print(f'RESULTADO: {arvore.buscar(100)}')
print(f'RESULTADO: {arvore.buscar(1)}')
print(f'RESULTADO: {arvore.buscar(10)}')
print(f'RESULTADO: {arvore.buscar(56)}')
