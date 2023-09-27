#Primero Función

def mediaTresNumeros(num1, num2, num3):
    resultado=(num1+num2+num3)/3
    return resultado
#------------------------------------------

#Después Código Principal-MAIN
    
print("Probando función")
a=1
b=2
c=3
media=mediaTresNumeros(a, b, c)
print(media)
media=mediaTresNumeros(20, 30, 40)
print(media)
print(mediaTresNumeros(a,20,c))
