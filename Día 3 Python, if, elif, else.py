#El input recoge el dato y lo guarda en el nombre.
nombre=input("Introduce tu nombre: ")
print("Hola "+nombre)

#Existen dos tipos de =s en programación:
#=-> Asigna lo que hay a la izquierda a lo que hay a la derecha.
#Ej. numero=5
# == -> Es un igual LÓGICO. ¡Compara los valores que tiene a izq y dcha! Devuelve true si son iguales o false si son distintas.
#Input siempre guarda el valor introducido como string.Si queremos que sea un int hay que transformarlo. int(input)(...))

#1. Entrada: edad. Salida: True si es mayor de edad.

edad=int(input("Introduce tu edad: "))
print("¿Es mayor de edad? ")
#Se puede escribir 'esMayorEdad=edad>=18'
esMayorEdad=edad>=18
print(esMayorEdad)
print(type(esMayorEdad))
#esMayorEdad es de tipo bool.
#Si ponemos "if edad>=18" en vez de "esMayorEdad" también funciona.
if esMayorEdad:
    print("Es mayor de edad")
    #Va tabulado, no con espacio.
#El "else" siempre tiene que ir debajo del "if".
else:
    print("Es menor de edad")
print("Se imprime siempre")
#Sin la variable bool esMayorEdad

#2. Entrada: Día de semana. Salida: True si fin de semana.

diaSemana=input("Introduce un día de la semana: ")
print("¿Es fin de semana?")
print(diaSemana=="sabado" or diaSemana=="domingo")

#3. Entrada: número. Salida: True si es positivo.

número=int(input("Introduce un número positivo: "))
print("¿Es un número positivo?")
esPositivo=(número>0)
if esPositivo:
    print("Es positivo")
if número==0:
    print("Es 0")
else:
    print("Es negativo")

#4. Entrada: Letra. Salida: True si es vocal.

letra=input("Introduce una letra: ")
print("¿Es vocal? ")
print(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u")

#5. Entrada: Número. Salida: True si está aprobado.

nota=int(input("Introduce tu nota: "))
print("¿Está aprobado?")

#Si no asumimos una nota válida.
#if nota>10 or nota <0:
#print("No es una nota válida")

#Si asumimos una nota válida.
#'if nota <=10 and nota >=9:'

Aprobado=(número>=5)
if nota>10 or nota <0:
    print("No es una nota válida")
elif nota<=10 and nota >=9:
    print("Sobresaliente")
elif nota <=8 and nota >=7:
    print("Notable")
elif nota>=6 and nota <7:
    print("bien")
elif nota>=5 and nota <6:
    print("Suficiente")
else:
    print("Suspenso")

