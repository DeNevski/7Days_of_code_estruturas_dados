class Paciente:
    def __init__(self, nome, num_identificacao, estado_atual):
        self.nome = nome
        self.num_identificacao = num_identificacao
        self.estado_atual = estado_atual
        self.proximo = None

class ListaDePacientes:
    def __init__(self):
        self.head = None

    # Adiciona novos pacientes ao final da lista
    def adicionar_paciente(self, nome, num_identificacao, estado_atual):
        if self.head:
            ponteiro = self.head
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            ponteiro.proximo = Paciente(nome, num_identificacao, estado_atual)
        else:
            self.head = Paciente(nome, num_identificacao, estado_atual)

    # Adiciona novos pacientes em uma posição desejada
    def inserir_paciente(self, indice, nome, num_identificacao, estado_atual):
        paciente = Paciente(nome, num_identificacao, estado_atual)
        if indice == 0:
            paciente.proximo = self.head
            self.head = paciente
        else:
            ponteiro = self.head
            for i in range(indice-1):
                if ponteiro:
                    ponteiro = ponteiro.proximo
                else:
                    raise IndexError('Indice não encontrado!')
            paciente.proximo = ponteiro.proximo
            ponteiro.proximo = paciente

    # Remove um paciente
    def remover_paciente(self, num):
        if self.head == None:
            raise ValueError('Você não tem um paciente cadastrado!')
        elif self.head.num_identificacao == num:
            self.head = self.head.proximo
            return True
        else:
            anterior = self.head
            ponteiro = self.head.proximo
            while ponteiro:
                if ponteiro.num_identificacao == num:
                    anterior.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                    return True
                anterior = ponteiro
                ponteiro = ponteiro.proximo
            raise ValueError('O código não foi encontrado!')

    # Lista todos pacientes
    def listar_pacientes(self):
        ponteiro = self.head
        while ponteiro:
            print(f'Nome: {ponteiro.nome:^10} Número de identificação: {ponteiro.num_identificacao:^5} Estado de saúde atual: {ponteiro.estado_atual:^10}')
            ponteiro = ponteiro.proximo  



pacientes = ListaDePacientes()

pacientes.adicionar_paciente('João', 100, 'estável')
pacientes.adicionar_paciente('Ana', 101, 'em observação')
pacientes.adicionar_paciente('Robson', 102, 'em tratamento intensivo')
pacientes.listar_pacientes()
print('\n')
pacientes.remover_paciente(100)
pacientes.listar_pacientes()
print('\n')
pacientes.inserir_paciente(0, 'Junior', 103, 'em recuperação')
pacientes.inserir_paciente(2, 'Cleiton', 104, 'estável')
pacientes.inserir_paciente(4, 'Pedro', 105, 'internado')
pacientes.remover_paciente(102)
pacientes.listar_pacientes()
