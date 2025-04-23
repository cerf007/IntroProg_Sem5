#Cálculo del consumo de agua por persona
consumo_agua = float(input("Ingrese la cantidad de agua en litros consumidos mensualmente en su vivienda: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que habitan en su casa:"))
consumo_mensual_pesrona = consumo_agua/cantidad_personas
consumo_diario = consumo_mensual_pesrona/30
print(f"""Consumo mensual del agua: {consumo_agua}
Personas en la viviendad: {cantidad_personas}
Consumo mensual promedio por persona:{consumo_mensual_pesrona:.2f}
Consumo diario promedio por persona:{consumo_diario:.2f}""")