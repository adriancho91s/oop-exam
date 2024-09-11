# Constantes para validar un número de 4 dígitos
MIN_4_DIGITOS = 1000
MAX_4_DIGITOS = 9999


def tiene_4_digitos(numero):
    """Verifica si el número tiene exactamente 4 dígitos."""
    return MIN_4_DIGITOS <= numero <= MAX_4_DIGITOS


def obtener_primer_digito(numero):
    """Obtiene el primer dígito de un número de 4 dígitos."""
    return numero // 1000


def obtener_segundo_digito(numero):
    """Obtiene el segundo dígito de un número de 4 dígitos."""
    return (numero // 100) % 10


def obtener_tercer_digito(numero):
    """Obtiene el tercer dígito de un número de 4 dígitos."""
    return (numero // 10) % 10


def obtener_cuarto_digito(numero):
    """Obtiene el cuarto dígito (último) de un número de 4 dígitos."""
    return numero % 10


def verificar_primer_digito_multiplo_del_cuarto(numero):
    """Verifica si el primer dígito es múltiplo del cuarto."""
    primer_digito = obtener_primer_digito(numero)
    cuarto_digito = obtener_cuarto_digito(numero)

    if cuarto_digito != 0 and primer_digito % cuarto_digito == 0:
        print(f"El primer dígito [{primer_digito}] es múltiplo del cuarto dígito [{cuarto_digito}].")
    else:
        print(f"El primer dígito [{primer_digito}] no es múltiplo del cuarto dígito [{cuarto_digito}].")


def sumar_segundo_y_tercer_digito(numero):
    """Suma el segundo y el tercer dígito de un número."""
    segundo_digito = obtener_segundo_digito(numero)
    tercer_digito = obtener_tercer_digito(numero)

    suma = segundo_digito + tercer_digito
    print(f"La suma del segundo dígito [{segundo_digito}] y el tercer dígito [{tercer_digito}] es: {suma}.")


def solicitar_numero_de_4_digitos():
    """Solicita al usuario un número de 4 dígitos válido."""
    while True:
        try:
            numero = int(input("Ingrese un número de 4 dígitos: "))
            if tiene_4_digitos(numero):
                return numero
            else:
                print("Número inválido. Por favor ingrese un número de 4 dígitos.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")


def ejecutar_operaciones_con_numero():
    """Ejecuta las operaciones sobre el número ingresado."""
    numero = solicitar_numero_de_4_digitos()
    verificar_primer_digito_multiplo_del_cuarto(numero)
    sumar_segundo_y_tercer_digito(numero)


# Llamada principal para iniciar el programa
if __name__ == "__main__":
    ejecutar_operaciones_con_numero()
