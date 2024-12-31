# Função responsável por receber uma aplicação e retornar sua respectiva descrição.
def descrever_aplicacao(aplicacao):
    if aplicacao == "reconhecimento de imagem":
        return "identificação e classificação de objetos em imagens"
    elif aplicacao == "processamento de linguagem natural":
        return "análise e interpretação de texto e fala"      
    elif aplicacao == "condução autônoma":
        return "controle de veículos sem intervenção humana"        
    elif aplicacao == "diagnóstico médico":
        return "análise de imagens médicas para detectar doenças"

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()
 
# Imprime a descrição da aplicação recebido na "entrada" através da função "descrever_aplicacao".
print(descrever_aplicacao(entrada))
