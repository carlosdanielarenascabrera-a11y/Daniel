precio_original = int(input("introduzca el precio: "))

valor_descuento = int(input("introduzca el descuento: "))

descuento_aplicado = (precio_original * valor_descuento) / 100

precio_final = precio_original - descuento_aplicado

print(f"precio original: {precio_original} descuento aplicado: {descuento_aplicado} precio final {precio_final} ")