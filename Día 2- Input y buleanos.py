#El input recoge el dato y lo guarda en el nombre.
nombre=input("Introduce tu nombre: ")
print("Hola "+nombre)

#Existen dos tipos de =s en programación:
#=-> Asigna lo que hay a la izquierda a lo que hay a la derecha.
#Ej. numero=5
# == -> Es un igual LÓGICO. ¡Compara los valores que tiene a izq y dcha! Devuelve true si son iguales o false si son distintas.
#Input siempre guarda el valor introducido como string.Formatter Si queremos que sea un int hay que transformarlo. int(input)(...))

#1. Entrada: Numero. Salida: True si es mayor de edad.

número=int(input("Introduce tu edad: "))
print("¿Es mayor de edad? ")
print(número>=18)

#2. Entrada: Día de semana. Salida: True si fin de semana.

diaSemana=input("Introduce un día de la semana: ")
print("¿Es fin de semana?")
print(diaSemana=="sabado" or diaSemana=="domingo")

#3. Entrada: número. Salida: True si es positivo.

número=int(input("Introduce un número positivo: "))
print("¿Es un número positivo?")
print(número>=0)

#4. Entrada: Letra. Salida: True si es vocal.

letra=input("Introduce una letra: ")
print("¿Es vocal? ")
print(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u")

#5. Entrada: Número. Salida: True si está aprobado.

número=int(input("Introduce tu nota: "))
print("¿Está aprobado?")
print(número>=5 and número <=10)
