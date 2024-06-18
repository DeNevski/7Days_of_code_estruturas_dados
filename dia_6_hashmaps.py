class Jogo:
    def __init__(self):
        self.dados = dict()

    # Adiciona um jogador no jogo
    def adicionar_jogador(self, usuario, pontos):
        self.dados[usuario] = pontos

    # Atualiza a pontuação de um jogador
    def atualizar_pontuacao(self, usuario, nova_pontuacao):
        if usuario not in self.dados:
            raise IndexError('Jogador não encontrado!')
        self.dados[usuario] = nova_pontuacao

    #Remove um jogador
    def remover_jogador(self, usuario):
        if usuario not in self.dados:
            raise IndexError('Jogador não encontrado!')
        del self.dados[usuario]

    # Lista todos os jogadores e suas pontuações
    def listar_jogadores(self):
        if len(self.dados) < 1:
            print('Sem jogadores no momento!')
        ranking = sorted(self.dados.items(), key=lambda x: x[1], reverse=True)
        print(f'{"JOGADOR:":<20} {"PONTUAÇÃO:":<20}')
        for k, v in ranking:
            print(f'{k:<20} {v:<20}')

    # Retorna o jogador vencedor com mais pontos
    def obter_vencedor(self):
        max_pts = max(self.dados.values())
        for k, v in self.dados.items():
            if max_pts == v:
                return f'O vencedor é {k} com {v} pontos.'



jogador = Jogo()
jogador.adicionar_jogador('NoCry', 350)
jogador.adicionar_jogador('DarkScorpion', 998)
jogador.adicionar_jogador('Master', 567)

jogador.atualizar_pontuacao('Master', 2000)

jogador.remover_jogador('DarkScorpion')

jogador.adicionar_jogador('Lord_Pro', 33)
jogador.adicionar_jogador('NoScope', 5874)
jogador.adicionar_jogador('XxGuerreiroxX', 967)

jogador.listar_jogadores()

print(jogador.obter_vencedor())
