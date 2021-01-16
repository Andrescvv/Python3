colones = float(input("Cuantos colones tienes?: "))

valor_dolar = 611.59

dolares = (colones / valor_dolar)
dolares = str(round(dolares, 2))

print("Tienes $" + dolares + " dolares")

