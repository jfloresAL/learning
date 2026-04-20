print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif opcion == "4":
    if num2 == 0:
        print("Error: No se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Opción no válida")