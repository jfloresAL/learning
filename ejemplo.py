

opcion = input("Elige una opción (1-4): ")

num1 = float(input("Ingresa numero1: "))
num2 = float(input("Ingresa número2: "))

if opcion == "1":
    resultado = num1 + num2
    print(resultado)

elif opcion == "2":
    resultado = num1 - num2
    print(resultado)

    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Opción no válida")
