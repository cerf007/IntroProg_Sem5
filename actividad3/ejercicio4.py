#Cálculo del consumo de combustible
distancia = float(input("Ingrese la distancia recorrida: "))
litros_con = float(input("Ingrese los litros consumidos: "))
precio_gasolina = float(input("Ingrese el precio por litro de gasolina: "))
total_combustible = litros_con * precio_gasolina 
rendimiento = distancia / litros_con
print(f"""Distancia recorrida: {distancia}
Litros consumidos: {litros_con}
Rendimiento del vehiculo: {rendimiento:.2f} km/lt
Precio total del combustible: {total_combustible}""")
