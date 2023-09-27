#Función
#num1, num2 y num3 son argumentos de entrada.
#Las 3 opciones están bien
def mediaTresNumeros(num1, num2, num3):
    resultado=(num1+num2+num3)/3
    return resultado
def otraMediaTresNumeros(num1, num2, num3): #Para dividir la operación final en más sencillas
    suma=num1+num2+num3
    return suma/3
def otraOtraMediaTresNumeros(num1, num2, num3): #Esta para operaciones sencillas.
    return(num1, num2, num3)/3
#Nunca en una función: (print)resultado
#Podemos tener funciones sin return
#Esto es una excepción, de normal no usamos print() en funciones, solo cuando el objetivo de la función sea mostrar algo.
def dibujaLinea(forma): #forma="="
    print(forma*20)
    #No return
def dibujaLineaPuntos():
    print("."*20)
    #Sin parámetros de entrada ni return
    #Para hacerlo sin print ():
def crearLinea(forma):
    return forma*20
def presentacion(nombre,edad):
    return ("Hola, soy jorge, tengo 21 años.")
#----------------------------------------

#Línea hecha con o minuscula, media de 5,10 y 15 es : 10 y otra línea hecha con O mayuscula.
dibujaLinea("o")
dibujaLinea("O")
media=mediaTresNumeros(5,10,15)
print ("La media de 5, 10 y 15 es: " + str(media))
print(f"La media es de {media}")

#Código q nos transmita un nombre y una edad.

nombre=input("Introduce tu nombre: ")
edad=input("Introduce tu edad: ")
print (presentacion(nombre,edad))


