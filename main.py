import classe
import datetime as dt
import csv

while classe.Pesquisa.querParticipar(aceitar) == True:

    nome = str(input("Informe o seu o nome: "))
    idade = int(input("Informe a sua idade: "))
    if idade > 00:
        genero = int(input("Informe qual o genero que você se identifica: "
                           "\n [1] Feminino\n [2] Masculino\n [3] Transgènero\n [4] Binário\n [5] Outro"))
    elif idade == 00:
        print("Fim da pesquisa.")
        break

rsp1 = int(input(f"Pergunta."
                 "[1] - Sim\n"
                 "[2] - Não\n"
                 "[3] - Não so responder\n"
                 "Escolha uma das alternativas."))
rsp2 = int(input(f"Pergunta."
                 "[1] - Sim\n"
                 "[2] - Não\n"
                 "[3] - Não so responder\n"
                 "Escolha uma das alternativas."))
rsp3 = int(input(f"Pergunta."
                 "[1] - Sim\n"
                 "[2] - Não\n"
                 "[3] - Não so responder\n"
                 "Escolha uma das alternativas."))
rsp4 = int(input(f"Pergunta."
                 "[1] - Sim\n"
                 "[2] - Não\n"
                 "[3] - Não so responder\n"
                 "Escolha uma das alternativas."))

dataHoraCadastrada = dt.datetime.now()

foiEntrevistado = classe.Pesquisa(nome, idade, genero, pergunta1Rsp, pergunta2Rsp, pergunta3Rsp, pergunta4Rsp, dataHoraCadastro)

primeiraResposta = foiEntrevistado.set_pergunta1(rsp1)
segundaResposta = foiEntrevistado.set_pergunta2(rsp2)
terceiraResposta = foiEntrevistado.set_pergunta3(rsp3)
quartaResposta = foiEntrevistado.set_pergunta4(rsp4)

print(dataHoraCadastrada.strftime('%d/%m/%Y %H:%M:%S'))
