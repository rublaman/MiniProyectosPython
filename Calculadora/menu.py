from Calculadora.operaciones import Operaciones


def menu_calculadora():
    print("Selecciona una operacion.")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dvididir")
    print("5. Modulo")
    print()

    op = Operaciones()
    opcion = 0
    valida = True

    while valida:
        opcion = int(input("Introduzca una operación del 1 al 4: "))
        if 0 < opcion > 6:
            print("Introduzca una opcion valida")
        else:
            valida = False
            print()

    num1 = float(input("Primer numero > "))
    num2 = float(input("Segundo numero > "))

    if opcion == 1:
        print(num1, "+", num2, "=", op.sumar(num1, num2))
    elif opcion == 2:
        print(num1, "-", num2, "=", op.restar(num1, num2))
    elif opcion == 3:
        print(num1, "*", num2, "=", op.multiplicar(num1, num2))
    elif opcion == 4:
        print(num1, "/", num2, "=", op.dividir(num1, num2))
    elif opcion == 5:
        print(num1, "%", num2, "=", op.modulo(num1, num2))
