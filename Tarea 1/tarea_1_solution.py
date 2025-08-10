
import string

def count_char(cadena, caracter):
    # a) Validar que cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # b) Validar que cadena solo contenga letras (a-z, A-Z) o dígitos (0-9)
    if not all(c.isalpha() or c.isdigit() for c in cadena):
        return -200, None

    # c) Validar que caracter sea un string de longitud 1 y que sea letra o dígito
    if not isinstance(caracter, str) or len(caracter) != 1 or not (caracter.isalpha() or caracter.isdigit()):
        return -300, None

    # d) Contar cantidad de veces que caracter aparece en cadena (case sensitive)
    cantidad = cadena.count(caracter)

    # e) Retornar código de éxito y cantidad
    return 0, cantidad

def multiplo_2(base, multiplo):
    # a) Validar que ambos sean enteros y no strings
    if not (isinstance(base, int) and isinstance(multiplo, int)):
        return -400, None
    if base < 0 or multiplo < 0:
        return -400, None

    # b) Validar que multiplo esté en [1, 2, 4, 8, 16]
    if multiplo not in [1, 2, 4, 8, 16]:
        return -500, None

    # c) Calcular usando desplazamiento de bits (equivalente a multiplicar por potencias de 2)
    #    Esto evita uso de sumas, multiplicaciones o bucles
    desplazamientos = {
        1: 0,
        2: 1,
        4: 2,
        8: 3,
        16: 4
    }
    resultado = base << desplazamientos[multiplo]

    # d) Retornar éxito y resultado
    return 0, resultado