num1 = int (input("introduzca un numero entero: "))

num2 = int (input("introduzca un numero entero: "))

num3 = int (input("introduzca un numero entero: "))

if num1 > num2 and num1 > num3:
    print (f"el numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print (f"el numero mayor es: {num2}")
else:
    print (f"el numero mayor es: {num3}")         