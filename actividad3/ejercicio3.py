#Cálculo de interés compuesto
capital_inicial = float(input("Ingrese su capital inicial: "))
interes_anual =  float(input("Ingrese la tasa porcentual del interes anual: "))
años = int(input("Ingrese la cantiad de años: "))
interes_decimal = interes_anual /100
monto_final = ((1 + interes_decimal)**años)*capital_inicial
interes_ganado =  monto_final - capital_inicial

print(f"""Capital inicial: {capital_inicial}
Tasa de interés anual: {interes_anual}
Años: {años}
Monto final: {monto_final:.0f}
Interés ganado: {interes_ganado:.0f}""")
