#SIMULADOR DE POUPANÇA--
aporte = float(input("Quanto você vai depositar no mês?"))
juros = float(input("Qual é a taxa atual de juros da poupança?"))
meses = int(input("Por quantos meses você vai investir?"))
juros_decimal = juros/100
total = 0
for mes in range(1,meses+1):
    total = total + aporte
    total = total + (total*juros_decimal)
    print(f"Mês{mes}:Saldo Total = R${total}")
print(f"Ao final de {meses} meses,você tera o valor de R${total:2f}")