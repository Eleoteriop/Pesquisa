import pandas as pd
import csv

class Pesquisa():
    def __init__(self, nome, idade, genero, pergunta1Rsp, pergunta2Rsp, pergunta3Rsp, pergunta4Rsp, dataHoraCadastro):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.pergunta1Rsp = pergunta1Rsp
        self.pergunta2Rsp = pergunta2Rsp
        self.pergunta3Rsp = pergunta3Rsp
        self.pergunta4Rsp = pergunta4Rsp
        self.dataHoraCadastro = dataHoraCadastro

    def querParticipar(self):
        aceitar = input("Quer participar desta pesquisa rápida? ")
        if aceitar.lower() == "SIM":
            return True
        elif aceitar.lower() == "NÃO":
            return False

    def receberDadosCandidatos(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero


    def receberGenero(self, genero):
        if genero == "F":
            self.genero = "Feminino"
            return self.genero
        elif genero == "M":
            self.genero = "Masculino"
            return self.genero
        elif genero == "T":
            self.genero = "Transgènero"
            return self.genero
        elif genero == "B":
            self.genero = "Binário"
            return self.genero
        elif genero == "O":
            self.genero = "Outro"
            return self.genero

    def set_pergunta1(self, resposta1):
        if resposta1 == 1:
            self.reposta1 = "Sim"
            return self.reposta1
        elif resposta1 == 2:
            self.resposta1 = "Não"
            return self.reposta1
        elif resposta1 == 3:
            self.resposta1 = "Não sei responder"
            return self.reposta1

    def set_pergunta2(self, resposta2):
        if resposta2 == 1:
            self.reposta2 = "Sim"
            return self.reposta2
        elif resposta2 == 2:
            self.resposta2 = "Não"
            return self.reposta2
        elif resposta2 == 3:
            self.resposta2 = "Não sei responder"
            return self.reposta2

    def set_pergunta3(self, resposta3):
        if resposta3 == 1:
            self.reposta3 = "Sim"
            return self.reposta3
        elif resposta3 == 2:
            self.resposta3 = "Não"
            return self.reposta3
        elif resposta3 == 3:
            self.resposta3 = "Não sei responder"
            return self.reposta3

    def set_pergunta4(self, resposta4):
        if resposta4 == 1:
            self.reposta4 = "Sim"
            return self.reposta4
        elif resposta4 == 2:
            self.resposta4 = "Não"
            return self.reposta4
        elif resposta4 == 3:
            self.resposta4 = "Não sei responder"
            return self.reposta4

    def DataHora(self, dataHoraCadastrada):
        self.dataHoraCadastrada = dataHoraCadastrada
        return dataHoraCadastrada

    def informacoesEntrevistado(self):
        resposta = [self.nome, self.idade, self.genero, self.resposta1,
                    self.resposta2, self.resposta3, self.resposta4]
        return resposta
