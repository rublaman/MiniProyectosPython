from Calculadora.operaciones import Operaciones


def menu_calculadora():
    print("\tSelecciona una operacion.")
    print("\t1. Sumar")
    print("\t2. Restar")
    print("\t3. Multiplicar")
    print("\t4. Dvididir")
    print("\t5. Modulo")
    print()

    op = Operaciones()
    opcion = 0
    valida = True

    while valida:
        opcion = int(input("Introduzca una operación del 1 al 5: "))
        if 0 < opcion > 6:
            print("Introduzca una opcion valida")
        else:
            valida = False
            print()

    num1 = float(input("\tPrimer numero > "))
    num2 = float(input("\tSegundo numero > "))
    print()

    if opcion == 1:
        print("\t", num1, "+", num2, "=", op.sumar(num1, num2), "\n")
    elif opcion == 2:
        print("\t", num1, "-", num2, "=", op.restar(num1, num2), "\n")
    elif opcion == 3:
        print("\t", num1, "*", num2, "=", op.multiplicar(num1, num2), "\n")
    elif opcion == 4:
        print("\t", num1, "/", num2, "=", op.dividir(num1, num2), "\n")
    elif opcion == 5:
        print("\t", num1, "%", num2, "=", op.modulo(num1, num2), "\n")
