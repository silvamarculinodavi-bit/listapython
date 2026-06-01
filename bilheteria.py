#aluno1: Padronizar nome do filme
def formatar(nome):
    return nome.upper()
#aluno2: Verificador de idade
def verificador(idade):
    if idade >= 18:
        return "Acesso permitido"
    else:
        return "Acesso Negado"
#aluno3: Mensagem de Retorno
def gerar_mensagem(status):
    if status == "Acesso permitido":
        return "Tenha uma ótima sessão!"
    else:
        return "Sentimos muito, mas você não tem idade minima."
#aluno4: Funçao do algoritmo
filme_enredo = input("Digite o filme escolhido: ")
idade_entrada = int(input("Digite sua idade: "))
nome_filme = formatar(filme_enredo)
status_acesso = verificador(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(f"Filme: {nome_filme}")
print(f"Status: {status_acesso}")
print(f"Mensagem: {mensagem}")