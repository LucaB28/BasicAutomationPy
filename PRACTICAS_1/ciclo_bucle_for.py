'''

for x in range(100):
    print("Luca" + str(x))



Colores = ["rojo","verde","amarillo"]

# LO QUE TENGA COLORES LO OBTIENE VCOL
for vcol in Colores:
    print(vcol)

# CICLO FOR LO QUE HACE EL BREAK ES DECIRLE EN QUE NUMERO ROMPERSE VA POR FUERA DEL FOR
for num in range (0,100,7):
    if(num >=75):
        break
    print(num)

'''
# FOR Y DETERMINAR QUE NUMERO NO IMPRIMIR

for num in range(1,11):
    if(num==3 or num == 6):
        continue
    print(num)