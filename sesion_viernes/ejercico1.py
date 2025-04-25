nota = float(input("Ingrese la calificación del alumno: "))
if nota >= 9 and nota<=10:
    print("La calificación es A")
elif nota >=7 and nota<=8:
    print("La califación es B")
elif nota>=5 and nota<=6:
    print("La calificación es C")
elif nota>=3 and nota<=4:
    print("La caficación es D")
elif nota>=0 and nota<=2:
    print("La calificación es F")
else: 
    print("La calificación es inválida")