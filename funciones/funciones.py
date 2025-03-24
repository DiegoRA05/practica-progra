def escribir_historial(operacion, resultado, archivo="historial"):
    """
    Registra la operación y el resultado en un archivo de historial.

    Args:
    operacion (str): Descripción de la operación realizada.
    resultado (str): Resultado de la operación.
    archivo (str): Ruta al archivo de historial.
    """
    with open(archivo, "a") as f:
        f.write(f"Operación: {operacion}\nResultado: {resultado}\n\n")

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
            else:
                polinomio_str += "-" if coef < 0 else ""
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
    resultado_str = mostrar_polinomio(resultado)

    print("\nResultado:")
    print(resultado_str)

    operacion_texto = "suma" if operacion == '+' else "resta"
    descripcion_operacion = f"{operacion_texto} de {mostrar_polinomio(p1)} y {mostrar_polinomio(p2)}"
    escribir_historial(descripcion_operacion, resultado_str)


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

    resultado_str = mostrar_polinomio(resultado)
    print("\nResultado:")
    print(resultado_str)

    descripcion_operacion = f"multiplicación de {mostrar_polinomio(p1)} y {mostrar_polinomio(p2)}"
    escribir_historial(descripcion_operacion, resultado_str)


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
        cociente.append(coef)

        for i in range(len(divisor)):
            residuo[i] -= coef * divisor[i]

        residuo.pop(0)

    cociente_str = mostrar_polinomio(cociente)
    residuo_str = mostrar_polinomio(residuo)
    print("\nCociente:")
    print(cociente_str)
    print("\nResiduo:")
    print(residuo_str)

    descripcion_operacion = f"división de {mostrar_polinomio(dividendo)} por {mostrar_polinomio(divisor)}"
    resultado_str = f"Cociente: {cociente_str}, Residuo: {residuo_str}"
    escribir_historial(descripcion_operacion, resultado_str)


def evaluar_polinomio():
    """Evalúa un polinomio en un valor dado."""
    print("\nPolinomio a evaluar:")
    p = ingresar_polinomio()
    x_valor = float(input("Introduce el valor de x: "))

    resultado = sum(coef * (x_valor ** (len(p) - i - 1)) for i, coef in enumerate(p))
    resultado_str = str(resultado)
    print(f"\nEl resultado de evaluar el polinomio en x = {x_valor} es: {resultado}")

    descripcion_operacion = f"evaluación de {mostrar_polinomio(p)} en x = {x_valor}"
    escribir_historial(descripcion_operacion, resultado_str)