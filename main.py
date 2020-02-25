from Calculadora.menu import menu_calculadora

opcion = 0
valida = True
run = True

while run:

    print('='*10 + " Selecciona una operacion " + '='*10)
    print("1. Adivina")
    print("2. Ahorcado")
    print("3. Calculadora")
    print("4. Dados")
    print("5. Salir")
    print()

    while valida:
        opcion = int(input("Seleccione la aplicacion a ejecutar: "))
        if 0 < opcion > 6:
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
        valida = True
    elif opcion == 4:
        pass
    elif opcion == 5:
        run = False
