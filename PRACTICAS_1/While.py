#Ciclo while , lo mismo que for pero sirve para poner que se
# cumpla hasta que pase algo

inicio = 1
fin = 10

#Break es para que lo saltee o no lo use

while (inicio <= fin):
    print("Esto se repite " + str(inicio))
    inicio=inicio+2
    if (inicio==6):
        break