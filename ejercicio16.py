anio = int (input("introduzca el anio: "))

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print (f"el anio {anio} es bisiesto ")
else:
    print (f"el anio {anio} no es bisiesto ")    