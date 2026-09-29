edad = int (input("digite su edad: "))

if edad >= 0 and edad <= 12:
    print ("clasificacion: Nino")
elif edad >= 13 and edad <= 17:
    print ("clasificacion: Adolescente")
elif edad >= 18 and edad <= 59:
    print ("clasificacion: Adulto")
else:
    print ("clasificacion: Adulto mayor")           