from funciones.funciones import (sumar_restar_polinomios, multiplicar_polinomios, dividir_polinomios, evaluar_polinomio, mostrar_polinomio, ingresar_polinomio)

def menu():
    """Menú de opciones de la calculadora de polinomios."""
    while True:
        print("\n--- Calculadora de Polinomios ---")
        print("1. Suma o resta")
        print("2. Multiplicación")
        print("3. División")
        print("4. Evaluación")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            sumar_restar_polinomios()
        elif opcion == '2':
            multiplicar_polinomios()
        elif opcion == '3':
            dividir_polinomios()
        elif opcion == '4':
            evaluar_polinomio()
        elif opcion == '5':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()