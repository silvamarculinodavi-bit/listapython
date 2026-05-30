#SIMULADOR DE INVESTIMENTO CDB--
print("=" * 30)
print("SIMULADOR DE INVESTIMENTO")
print("Versão 1.0 - Desenvolvido no Codespace")
print("=" * 30)
print(" ")
aporte = float(input("Quanto você vai depositar no mês?"))
print("Juros do CBD: 1.24")
meses = int(input("Por quantos meses você vai investir?"))
juros_decimal = 1.24/100
total = 0
for mes in range(1,meses+1):
    total = total + aporte
    total = total + (total*juros_decimal)
    print(f"Mês{mes}:Saldo Total = R${total}")
print(f"Ao final de {meses} meses,você tera o valor de R${total:2f}")
#Davi da Silva Marculino--