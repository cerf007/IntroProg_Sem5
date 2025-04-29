def EsTriangulo(lado_1, lado_2, lado_3):
    suma = lado_1 + lado_2
    if (suma > lado_3):
        return "Es un triángulo"
    else: 
        return "No es un triángulo"
def main():
        print("Ingresa los siguientes valores:")
        print("="*30)
        lado_1= float(input("Lado 1:"))
        lado_2= float(input("Lado 2:")) 
        lado_3= float(input("Lado 3:"))
        print(EsTriangulo(lado_1, lado_2, lado_3))
            
main()