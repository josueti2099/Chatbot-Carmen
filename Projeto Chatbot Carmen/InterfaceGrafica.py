import ProjetoChatbot as pc
from tkinter import *

main_window = Tk()

main_window.title("Carmen")
main_window.geometry("500x700")


frame = Frame(main_window)
frame.grid()

l_identif = Label(frame, text="Insira uma mensagem para a Carmen: ")
l_identif.grid(row=0, column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)

frame2 = Frame(main_window)
frame2.grid(row=1, column=0)
v = StringVar()
Label(frame2, textvariable=v).grid()

nome_maquina = "Carmen"

v.set("Qual é o seu nome?")
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""
historico_conversa = ""


def roda_Chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario

    palavraProibida = ["bobo", "burro", "idiota", "feio",
                       "inútil", "chato", "chata", "otário", "otária", "imbecil"]

    if entrada_nome_usuario:
        nome_usuario = e_mensagem.get()
        saudacao = pc.saudacoes_GUI(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        v.set(historico_conversa)
        entrada_nome_usuario = False
        e_mensagem.delete(0, END)  # Limpa o campo de texto
    else:
        texto = e_mensagem.get().lower()

        if any(p in texto for p in palavraProibida):
            historico_conversa += "\n " + nome_usuario + ": " + texto
            historico_conversa += "\n Carmen: Por favor, mantenha o respeito durante a conversa.\n"
            v.set(historico_conversa)
            e_mensagem.delete(0, END)
            return

        historico_conversa += "\n " + nome_usuario + ": " + texto
        v.set(historico_conversa)

        if entrada_sugestao:
            pc.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += "\n Agora aprendi! Vamos continuar a nossa conversa... \n"
            v.set(historico_conversa)
            e_mensagem.delete(0, END)
        else:
            resposta = pc.buscaResposta_GUI("cliente: " + texto + "\n")
            if resposta == "Me desculpe, não sei o que falar":
                historico_conversa += "\n Me desculpe, não sei o que falar. O que você esperava? \n"
                v.set(historico_conversa)
                entrada_sugestao = True
            else:
                historico_conversa += "\n" + \
                    pc.exibeResposta_GUI(texto, resposta, nome_maquina)
                v.set(historico_conversa)
            e_mensagem.delete(0, END)


Button(frame, text="Enviar", command=roda_Chatbot).grid(row=0, column=2)

main_window.mainloop()
