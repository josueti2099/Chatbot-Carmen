def saudacoes_GUI(nome):
    import random
    frases = ["Olá, meu nome é " + nome +
              "Como posso te ajudar?", "Olá!", "Oi, tudo bem?"]
    return frases[random.randint(0, len(frases)-1)]


def recebeTexto():
    palavraProibida = ["boba", "burra", "feia",
                       "idiota", "imbecil", "otaria", "inutil"]

    while True:
        texto = input("cliente: ").lower()

        if any(p in texto for p in palavraProibida):
            print("Por favor, mantenha o respeito durante a conversa.")
        else:
            return texto


def buscaResposta_GUI(texto):
    melhor_resposta = "Me desculpe, não sei o que falar"
    maior_confianca = 0.0

    try:
        with open("base.txt", "r", encoding='utf-8') as conhecimento:
            linhas = conhecimento.readlines()
    except FileNotFoundError:
        with open("base.txt", "w", encoding='utf-8') as criar:
            pass
        return melhor_resposta

    for i in range(0, len(linhas), 2):
        if i + 1 < len(linhas):
            pergunta_base = linhas[i]
            resposta_base = linhas[i + 1]

            confianca = jaccard(texto, pergunta_base)
            if confianca > maior_confianca:
                maior_confianca = confianca
                melhor_resposta = resposta_base
    if maior_confianca >= 0.8:
        return melhor_resposta
    else:
        with open("base.txt", "a+", encoding='utf-8') as conhecimento:
            conhecimento.write(texto.strip() + "\n")
        return "Me desculpe, não sei o que falar"
    # with open("base.txt", "a+", encoding='utf-8') as conhecimento:
        # conhecimento.seek(0)
        # while True:
        # viu = conhecimento.readline()
        # if viu != "":
        # if jaccard(texto, viu) > 0.3:
        # proximalinha = conhecimento.readline()
        # if "chatbot: " in proximalinha:
        #        return proximalinha
        # else:
        # conhecimento.write(texto)
        # return "Me desculpe, não sei o que falar"


def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("chatbot: ", nome + ": ")

    if resposta == "fim":
        return "fim"
    return "continue"


def salva_sugestao(sugestao):
    with open("base.txt", "a+", encoding='utf-8') as conhecimento:
        conhecimento.write("chatbot: " + sugestao.strip() + "\n")


def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum / (len(textoBase.split()))


def limpa_frase(frase):
    tirar = ["?", "!", "...", ".", ",", "cliente: ",
             "\n", ":", ";", "-", "_", "()", "*"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase
