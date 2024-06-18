from re import match
from sys import exit
from time import sleep

cores = {
'vermelho':'\033[1;31m',
'verde':'\033[1;32m',
'amarelo':'\033[1;33m',
'branco':'\033[1;97m',
'ciano':'\033[1;36m',
'limitar':'\033[m'
}


class ListaDeCompras:
    def __init__(self):
        self.produtos = list()
        self.quantidades = list()
        self.opcoes()

    # Exibe o menu de opções e redireciona para a opção desejada
    def opcoes(self):
        print(f'{cores["branco"]}[1] Adicionar Novo Item \n[2] Remover Item \n[3] Listar Itens \n[4] Sair{cores["limitar"]}')

        while True:
            try:
                escolha = int(input(f'{cores["amarelo"]}O que deseja fazer? {cores["limitar"]}'))
                if escolha < 1 or escolha > 4:
                    raise Exception
            except (ValueError, TypeError, Exception):
                print(f'{cores["vermelho"]}Opção inválida!{cores["limitar"]}')
            else:
                if escolha == 1:
                    self.adicionar_item()
                elif escolha == 2:
                    self.remover_item()
                elif escolha == 3:
                    self.listar_itens()
                elif escolha == 4:
                    print(f'{cores["vermelho"]}Saindo...{cores["limitar"]}')
                    exit()

    # Adiciona itens na lista
    def adicionar_item(self):
        while True:
            try:
                produto = str(input(f'{cores["amarelo"]}Nome do produto: {cores["limitar"]}')).strip().capitalize()
                if not match(r'^[A-Z-a-z-À-ÿ\s]+$', produto):
                    raise Exception
                quantidade = int(input(f'{cores["amarelo"]}Quantidade: {cores["limitar"]}'))
                if quantidade < 0:
                    raise ValueError
            except (TypeError, ValueError):
                print(f'{cores["vermelho"]}Quantidade inválida!{cores["limitar"]}')
            except Exception:
                print(f'{cores["vermelho"]}Esse produto não é válido!{cores["limitar"]}')
            else:
                self.produtos.append(produto)
                self.quantidades.append(quantidade)
                print(f'{cores["verde"]}Produto adicionado com sucesso!{cores["limitar"]}')
                sleep(0.75)
                print('')
                self.opcoes()

    # Remove itens da lista
    def remover_item(self):
        try:
            produto = str(input(f'{cores["amarelo"]}Deseja remover qual produto? {cores["limitar"]}')).strip().capitalize()
            if not produto in self.produtos:
                raise ValueError
            for i, v in enumerate(self.produtos):
                if v == produto:
                    del self.produtos[i]
                    del self.quantidades[i]
        except ValueError:
            print(f'{cores["vermelho"]}Esse produto não está na sua lista!{cores["limitar"]}')
            print('')
        else:
            print(f'{cores["verde"]}Produto removido com sucesso!{cores["limitar"]}')
            print('')
        finally:
            sleep(0.75)
            self.opcoes()

    # Lista todos os itens que estão na lista
    def listar_itens(self):
        print(f'{cores["branco"]}{"Produto:":<20} {"Quantidade:":<20}{cores["limitar"]}')
        for i in range(len(self.produtos)):
            print(f'{cores["ciano"]}{self.produtos[i]:<20} {self.quantidades[i]:<20}{cores["limitar"]}')
            sleep(1)
        print('')
        self.opcoes()


lista = ListaDeCompras()
lista.opcoes()
