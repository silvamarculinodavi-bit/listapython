#--simulador de investimento--
deposito_mensal = 50
total = 0
for mes in range(1,7):
    total = total + deposito_mensal
    print(f"Mês {mes} :Saldo total = R${total}")
print(f"Ao final de 6 meses, você terá R${total}")