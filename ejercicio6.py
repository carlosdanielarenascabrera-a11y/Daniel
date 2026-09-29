segundos = int(input("introduzca los segundos: "))

horas = segundos // 3600

resto = segundos % 3600

minutos = resto // 60



segundos_restantes = resto % 60

print (f"{horas} horas {minutos} minutos {segundos_restantes} segundos")