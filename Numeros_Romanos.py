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
permitidos_restar = {"i": ["v", "x"], "x": ["l", "c"], "c": ["d", "m"]}
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
                j0, j1 = caracteres[i], caracteres[i + 1]
                if valores_romanos[j0] < valores_romanos[j1]:
                    if j0 not in permitidos_restar or j1 not in permitidos_restar[j0]:
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
            valores = [valores_romanos[i] for i in caracteres]
            resultado = 0

            for i in range(len(valores)):
                if i < len(valores) - 1 and valores[i] < valores[i + 1]:  # Si el valor actual es menor que el siguiente, se resta
                    resultado -= valores[i]
                else:
                    resultado += valores[i]

        if caracter_invalido == 1:
            print("Error de Caracteres: No ha ingresado un número romano válido.")
        elif caracter_invalido == 2:
            print("Error de Resta: I puede restarse de V y X; X puede restarse de L y C; y C puede restarse de D y M. Las demas restas no son válidas.")
        elif caracter_invalido == 3:
            print("Error de Repetición: I, X, C y M solo se pueden repetir hasta tres veces y V, L y D no pueden repetirse.")
        else:
            print(f"El número romano ingresado es equivalente a: {resultado}.")

print("Fin del programa.")