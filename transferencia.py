propietario = input("Nombre del propietario: ")
mascota = input("Nombre de la mascota: ")

consulta = float(input("Valor de la consulta: "))
medicamentos = float(input("Valor de los medicamentos: "))
otros_servicios = float(input("Valor de otros servicios: "))

total = consulta + medicamentos + otros_servicios

print("\n------ FACTURA VETERINARIA ------")
print("Propietario:", propietario)
print("Mascota:", mascota)
print("Consulta: $", consulta)
print("Medicamentos: $", medicamentos)
print("Otros servicios: $", otros_servicios)
print("-------------------------------")
print("TOTAL A PAGAR: $", total)