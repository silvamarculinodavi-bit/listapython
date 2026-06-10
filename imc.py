#calculo do imc--
def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

#classificar o imc--
def classificar_imc(valor_imc):
    if valor_imc >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"

#mensagem de saida--
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "Procure um Médico"
    else:
        return "Continue assim"

valor_peso = float(input("Qual seu peso? "))
valor_altura = float(input("Qual a sua altura? "))
calculo = calculo_imc(valor_peso, valor_altura)
classificar = classificar_imc(calculo)
mensagem_valor = mensagem(classificar)
print(mensagem_valor)