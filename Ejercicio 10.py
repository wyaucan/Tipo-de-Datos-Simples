#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

monto = int(input("Ingrese el momento a invertir: "))
i = float(input("Ingrese el interes anual: "))
a = int(input("Interese los año a invertir: "))

total_inversion = monto*i
interes = total_inversion-monto
total_anual = total_inversion*a
print()
print("El Monto de la inversion es: ", monto)
print("El intereses es: ", interes)
print("El total de la inversion es: ", total_inversion)
print("El total de la inversion de los años seleccionado es: ", total_anual)