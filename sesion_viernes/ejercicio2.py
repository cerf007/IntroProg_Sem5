sueldo = float(input("Ingrese el sueldo: "))
bono = 0
if sueldo>3000:
    bono = sueldo *10/100
elif sueldo>1500 and sueldo<3000:
    bono = sueldo * 5/100
elif sueldo<=1500:
    bono = 0

print(f"Su sueldo es: {sueldo}")
print(f"Su bono es: {bono}")
print(f"Su sueldo total es:  {sueldo + bono}")
    
