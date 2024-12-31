# Função responsável por receber um tipo de rede e retornar sua respectiva descrição.
def descrever_rede(rede):
    if rede == "redes neurais convolucionais":
        return "especializadas em processamento de imagens"                                
    elif rede == "redes neurais recorrentes":
        return "projetadas para processar dados sequenciais"
    elif rede == "redes neurais de memória de longa e curta duração":
        return "podem aprender dependências de longo prazo em dados sequenciais"
    elif rede == "autoencoders":
        return "usadas para compressão e reconstrução de dados"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Imprime a descrição do tipo de rede recebido na "entrada" através da função "descrever_rede".
print(descrever_rede(entrada))
