num1 = int (input("introduzca un numero: "))

num2 = int (input("introduzca un numero: "))

print ("1. sumar")
print ("2. restar")
print ("3. mulitiplicar")
print ("4. dividir")

operacion = int (input("introduzca la operacion que desea: "))

if operacion == 1:
    resultado = num1 + num2
    print (f"resultado: {resultado}")
elif operacion == 2:
     resultado = num1 - num2
     print (f"resultado: {resultado}")
elif operacion == 3:
    resultado = num1 * num2
    print (f"resultado: {resultado}")
elif operacion == 4:
    resultado = num1 / num2
    print (f"resultado: {resultado}")
