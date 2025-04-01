# Algoritmo para calcular el IMC (Índice de Masa Corporal)

# Mensaje de bienvenida
print("*****BIENVENIDO*****")

# Preguntar si quiere calcular el IMC
print("¿Quiere calcular su índice de masa corporal?")
print("Escribe 1 si es sí, escribe 2 si es no")
cal_indice = int(input())  # Leemos la respuesta del usuario

# Si el usuario responde que sí
if cal_indice == 1:
    # Pedir la estatura y el peso
    print("Ingresa tu estatura en metros (M):")
    estatura = float(input())  # Leemos la estatura

    print("Ingresa tu peso en kilogramos (KG):")
    peso = float(input())  # Leemos el peso

    # Calcular el IMC
    indice = peso / (estatura * estatura)

    # Mostrar el resultado
    print(f"Su índice de masa corporal es: {indice:.2f}")

# Si el usuario no quiere calcular el IMC
else:
    print("Gracias por su visita")

