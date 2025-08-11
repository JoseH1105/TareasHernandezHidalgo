
def count_char(cadena, caracter):
    """
    Cuenta cuántas veces aparece un carácter específico en una cadena.

    Parámetros:
    cadena (str): Cadena que se desea evaluar.
    caracter (str): Carácter que se desea contar.

    Retorna:
    tuple: (codigo, cantidad)
        codigo (int): Código de éxito o error.
             0 -> éxito
            -100 -> cadena no es un string
            -200 -> cadena contiene caracteres no permitidos
            -300 -> parámetro caracter inválido
        cantidad (int or None): Cantidad de veces que el carácter aparece.
            None en caso de error.
    """
    # a) Validar que cadena sea un string
    if not isinstance(cadena, str):
        return -100, None

    # b) Validar que cadena solo contenga letras o dígitos
    if not all(c.isalpha() or c.isdigit() for c in cadena):
        return -200, None

    # c) Validar que caracter sea string de un solo carácter válido
    if not isinstance(caracter, str) or len(caracter) != 1:
        return -300, None
    if not (caracter.isalpha() or caracter.isdigit()):
        return -300, None

    # d) Contar cantidad de veces que caracter aparece en cadena
    cantidad = cadena.count(caracter)

    # e) Retornar código de éxito y cantidad
    return 0, cantidad


def multiplo_2(base, multiplo):
    """
    Multiplica un número base por un múltiplo permitido.

    Parámetros:
    base (int): Número entero positivo.
    multiplo (int): Múltiplo permitido (1, 2, 4, 8, 16).

    Retorna:
    tuple: (codigo, resultado)
        codigo (int): Código de éxito o error.
            0 -> éxito
            1 -> parámetros no son enteros positivos
            2 -> múltiplo no permitido
        resultado (int or None): Resultado de la operación
    """
    # a) Validar que ambos sean enteros positivos (o cero)
    if not (isinstance(base, int) and isinstance(multiplo, int)):
        return -400, None
    if base < 0 or multiplo < 0:
        return -400, None

    # b) Validar que multiplo esté en [1, 2, 4, 8, 16]
    valores_validos = [1, 2, 4, 8, 16]
    if multiplo not in valores_validos:
        return -500, None

    # c) Calcular usando desplazamiento de bits (sin *, + ni bucles)
    desplazamientos = {
        1: 0,
        2: 1,
        4: 2,
        8: 3,
        16: 4
    }
    resultado = base << desplazamientos[multiplo]

    # d) Retornar código de éxito y resultado
    return 0, resultado
