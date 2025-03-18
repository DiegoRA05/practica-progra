def ingresar_polinomio():
    """Solicita al usuario el grado del polinomio y sus coeficientes."""
    grado = int(input("Introduce el grado del polinomio: "))
    coeficientes = []
    for i in range(grado, -1, -1):
        coef = float(input(f"Coeficiente para x^{i}: "))
        coeficientes.append(coef)
    return coeficientes


def mostrar_polinomio(coeficientes):
    """Convierte la lista de coeficientes en una representación de cadena de un polinomio."""
    polinomio_str = ""
    for i, coef in enumerate(coeficientes):
        exponente = len(coeficientes) - i - 1
        if coef != 0:
            if polinomio_str:
                polinomio_str += " + " if coef > 0 else " - "
            polinomio_str += f"{abs(coef)}x^{exponente}" if exponente > 0 else f"{abs(coef)}"
    return polinomio_str if polinomio_str else "0"


def sumar_restar_polinomios():
    """Suma o resta dos polinomios representados como listas."""
    print("\nPrimer polinomio:")
    p1 = ingresar_polinomio()
    print("\nSegundo polinomio:")
    p2 = ingresar_polinomio()

    operacion = input("\n¿Quieres sumar (+) o restar (-) los polinomios? ").strip()
    if operacion not in ('+', '-'):
        print("Operación no válida.")
        return

    max_grado = max(len(p1), len(p2))
    p1 = [0] * (max_grado - len(p1)) + p1
    p2 = [0] * (max_grado - len(p2)) + p2

    resultado = [(p1[i] + p2[i]) if operacion == '+' else (p1[i] - p2[i]) for i in range(max_grado)]

    print("\nResultado:")
    print(mostrar_polinomio(resultado))


def multiplicar_polinomios():
    """Multiplica dos polinomios representados como listas."""
    print("\nPrimer polinomio:")
    p1 = ingresar_polinomio()
    print("\nSegundo polinomio:")
    p2 = ingresar_polinomio()

    resultado = [0] * (len(p1) + len(p2) - 1)

    for i in range(len(p1)):
        for j in range(len(p2)):
            resultado[i + j] += p1[i] * p2[j]

    print("\nResultado:")
    print(mostrar_polinomio(resultado))


def dividir_polinomios():
    """Divide dos polinomios y devuelve el cociente y el residuo."""
    print("\nDividendo:")
    dividendo = ingresar_polinomio()
    print("\nDivisor:")
    divisor = ingresar_polinomio()

    if len(divisor) == 1 and divisor[0] == 0:
        print("Error: División entre cero.")
        return

    cociente = []
    residuo = dividendo[:]

    while len(residuo) >= len(divisor):
        coef = residuo[0] / divisor[0]
        grado_diff = len(residuo) - len(divisor)
        cociente.append(coef)

        # Restar el polinomio divisor escalado
        for i in range(len(divisor)):
            residuo[i] -= coef * divisor[i]

        residuo.pop(0)

    print("\nCociente:")
    print(mostrar_polinomio(cociente))
    print("\nResiduo:")
    print(mostrar_polinomio(residuo))


def evaluar_polinomio():
    """Evalúa un polinomio en un valor dado."""
    print("\nPolinomio a evaluar:")
    p = ingresar_polinomio()
    x_valor = float(input("Introduce el valor de x: "))

    resultado = sum(coef * (x_valor ** (len(p) - i - 1)) for i, coef in enumerate(p))

    print(f"\nEl resultado de evaluar el polinomio en x = {x_valor} es: {resultado}")