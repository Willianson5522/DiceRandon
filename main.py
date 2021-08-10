import random

reposta = 0

def pergunta():
    global resposta
    resposta = input("Você gostaria de jogar o dado? (s/n)\n")
    verificar_resposta()
    
def verificar_resposta():
    global resposta
    if resposta.casefold() == "s":
        print("Dado diz:",random.randint(1,6))
        resposta = input("Jogar novamente?\n")
        return verificar_resposta()

    if resposta.casefold() == "n":
        print("Encerrando programa...")
        print("Encerrado.")
        exit
        
    else:
        resposta = input("Resposta inválida, responda entre (s/n)\n" )
        verificar_resposta()

pergunta()

