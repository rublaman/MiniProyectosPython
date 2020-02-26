from Calculadora.menu import menu_calculadora

op_menu = 0
valida = True
run = True

while run:

    print('=' * 10 + " Selecciona una operacion " + '=' * 10)
    print("1. Adivina")
    print("2. Ahorcado")
    print("3. Calculadora")
    print("4. Dados")
    print("5. Salir")
    print()

    while valida:
        op_menu = int(input("Seleccione la aplicacion a ejecutar: "))
        if 0 < op_menu > 6:
            print("Introduzca una opcion valida")
        else:
            valida = False
            print()

    if op_menu == 1:
        pass
    elif op_menu == 2:
        pass
    elif op_menu == 3:
        menu_calculadora()
        valida = True
    elif op_menu == 4:
        pass
    elif op_menu == 5:
        run = False
