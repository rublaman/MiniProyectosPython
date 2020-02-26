from Calculadora.operaciones import Operaciones


def menu_calculadora():
    operacion = Operaciones()

    valida = True
    run_calculadora = True

    while run_calculadora:

        print("\tSelecciona una operacion.")
        print("\t1. Sumar")
        print("\t2. Restar")
        print("\t3. Multiplicar")
        print("\t4. Dvididir")
        print("\t5. Modulo")
        print("\t6. Salir de la calculadora")
        print()

        op_menu_calc = -1

        while valida:
            op_menu_calc = int(input("Introduzca una operación del 1 al 6: "))
            if 0 < op_menu_calc > 6:
                print("Introduzca una opcion valida")
            else:
                valida = False
                print()

        if op_menu_calc == 6:
            run_calculadora = False
        else:
            num1 = float(input("\tPrimer numero > "))
            num2 = float(input("\tSegundo numero > "))
            print()

            if op_menu_calc == 1:
                print("\t", num1, "+", num2, "=", operacion.sumar(num1, num2), "\n")
                valida = True
            elif op_menu_calc == 2:
                print("\t", num1, "-", num2, "=", operacion.restar(num1, num2), "\n")
                valida = True
            elif op_menu_calc == 3:
                print("\t", num1, "*", num2, "=", operacion.multiplicar(num1, num2), "\n")
                valida = True
            elif op_menu_calc == 4:
                print("\t", num1, "/", num2, "=", operacion.dividir(num1, num2), "\n")
                valida = True
            elif op_menu_calc == 5:
                print("\t", num1, "%", num2, "=", operacion.modulo(num1, num2), "\n")
                valida = True
