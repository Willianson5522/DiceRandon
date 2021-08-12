import random

def pergunta():
    resposta = input("Você gostaria de jogar o dado? (s/n)\n")
    verificar_resposta(resposta)
    
def verificar_resposta(parametro):
    if parametro.casefold() == "s" or parametro.casefold() == "sim":
        print("Dado diz:",random.randint(1,6))
        resposta = input("Jogar novamente? (s/n)\n")
        verificar_resposta(resposta)

    elif parametro.casefold() == "n" or parametro.casefold() == "não":
        print("Encerrando programa...")
        print("Encerrado.")
        exit
        
    else:
        resposta = input("Resposta inválida, responda entre (s/n)\n" )
        verificar_resposta(resposta)

pergunta()


