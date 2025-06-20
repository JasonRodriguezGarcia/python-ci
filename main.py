from mathematics import add, multiply

if __name__=='__main__':
    print("""
       Bienvenido a nuestro
       Programa de matematicas
    """)
    print("Main program para ayudarle con las mates")
    accion = input("Qué quieres hacer? s- suma, m- multiplica: ")

    numero1 = int(input("Primer número: "))
    numero2 = int(input("Segundo número: "))

    if accion == 's':
        result = add(numero1, numero2)
        print(f"Suma: {result}")
    else:
        print("Multiplicacion: ", multiply(numero1, numero2))
