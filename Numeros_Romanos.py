# El Programa debe leer el input del usuario y convertir los Números Romanos a Números arábigos modernos.
# Para ello, voy a hacer un código que haga tres cosas:
#    Crear un loop que no finalice el programa hasta que el usuario escriba "Fin" o una variación.
#    Detectar si el input es un número romano o no es un número romano romano.
#        En caso de no ser un número romano, aclararle al usuario su error.
#    Convertir el input de un número romano a un número arábigo.

print("Escriba 'Fin' para finalizar el programa.")

entrada = ""
caracteres = []
valores_romanos = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
permitidos_restar = ["i", "x", "c"]
no_repetibles = ["v", "l", "d"]

while entrada not in ["fin", "'fin'", "'fin", "fin'"]:
    caracteres.clear()
    caracter_invalido = 0

    entrada = input("Ingresa un número romano: ").strip().lower()

    if entrada not in ["fin", "'fin'", "'fin", "fin'"]:
        caracteres = [i for i in entrada if i != " "]

        for i in caracteres:
            if i not in valores_romanos:
                caracter_invalido = 1
                break

        if caracter_invalido == 0:
            for i in range(len(caracteres) - 1):
                j0 = caracteres[i]
                j1 = caracteres[i + 1]

                if valores_romanos[j0] < valores_romanos[j1]:
                    if j0 not in permitidos_restar or j1 in no_repetibles:
                        caracter_invalido = 2
                        break

        if caracter_invalido == 0:
            j = 1
            for i in range(1, len(caracteres)):
                if caracteres[i] == caracteres[i - 1]:
                    j += 1
                    if caracteres[i] in no_repetibles or j > 3:
                        caracter_invalido = 3
                        break
                else:
                    j = 1

        if caracter_invalido == 0:
            caracteres = [valores_romanos[i] for i in caracteres]

        if caracter_invalido == 1:
            print("No ha ingresado un número romano válido.")
        elif caracter_invalido == 2:
            print("Solo I, X y C pueden restarse.")
        elif caracter_invalido == 3:
            print("I, X, C y M solo se pueden repetir hasta tres veces y V, L y D no pueden repetirse.")
        else:
            print(caracteres)

print("Fin del programa.")