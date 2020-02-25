from Calculadora.menu import menu_calculadora

print("Selecciona una operacion.")
print("1. Adivina")
print("2. Ahorcado")
print("3. Calculadora")
print("4. Dados")
print()

opcion = 0
valida = True

while valida:
    opcion = int(input("Seleccione la aplicacion a ejecutar: "))
    if 0 < opcion > 5:
        print("Introduzca una opcion valida")
    else:
        valida = False
        print()

if opcion == 1:
    pass
elif opcion == 2:
    pass
elif opcion == 3:
    menu_calculadora()
elif opcion == 4:
    pass
