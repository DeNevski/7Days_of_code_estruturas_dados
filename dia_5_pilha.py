class Livro:
    def __init__(self, nome_livro, total_paginas):
        self.nome_livro = nome_livro
        self.total_paginas = total_paginas

class PilhaDeLivros:
    def __init__(self):
        self.pilha_de_livros = []

    # Adiciona novos livros na pilha
    def adicionar_livro(self, nome_livro, total_paginas):
        novo_livro = Livro(nome_livro, total_paginas)
        self.pilha_de_livros.append(novo_livro)

    # Remove livros da pilha
    def remover_livro(self):
        if len(self.pilha_de_livros) > 0:
            return self.pilha_de_livros.pop().nome_livro
        else:
            raise IndexError('Não há nada empilhado por aqui...')
     
    # Retorna qual livro está no topo da pilha
    def livro_do_topo(self):
        if len(self.pilha_de_livros) > 0:
            topo = self.pilha_de_livros[-1]
            return f'O livro no topo da pilha é {topo.nome_livro} com {topo.total_paginas} páginas.'
        else:
            raise IndexError('Não há nada empilhado por aqui...')
    
    # Lista todos os livros que estão na pilha
    def listar_livros(self):
        if len(self.pilha_de_livros) < 1:
            print('Oops! Nada empilhado por aqui.')
        for livro in reversed(self.pilha_de_livros):
            print(f'Nome do livro: {livro.nome_livro:^40} Total de páginas: {livro.total_paginas:^5}')
        


pilha = PilhaDeLivros()
pilha.adicionar_livro('Código Limpo', 425)
pilha.adicionar_livro('Python Fluente', 800)
pilha.adicionar_livro('Pai Rico Pai Pobre', 336)
pilha.listar_livros()
print('\n')
print(pilha.remover_livro())
print('\n')
print(pilha.livro_do_topo())
print('\n')
pilha.adicionar_livro('Mentes Brilhantes, Mentes Treinadas', 80)
pilha.listar_livros()
print('\n')
pilha.remover_livro()
pilha.remover_livro()
pilha.remover_livro()
pilha.listar_livros()

