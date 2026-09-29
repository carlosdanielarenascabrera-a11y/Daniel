lado1 = int (input("introduzca la longitud del primer lado: "))

lado2 = int (input("introduzca la longitud del segundo- lado: "))

lado3 = int (input("introduzca la longitud del tercer lado: "))


if  lado1 == lado2 and lado2 == lado3:
    print ("el triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
      print ("el triangulo es isosceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
      print ("el triangulo es escaleno")    
