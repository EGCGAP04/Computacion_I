# El Programa debe leer el input del usuario y convertir los Números Romanos a Números arábigos modernos.
# Para ello, voy a hacer un código que haga tres cosas:
#    Crear un loop que no finalice el programa hasta que el usuario escriba "Fin" o una variación.
#    Detectar si el input es un número romano o no es un número romano romano.
#        En caso de no ser un número romano, aclararle al usuario su error.
#    Convertir el input de un número romano a un número arábigo.

print("Escriba 'Fin' para finalizar el programa.")

entrada = ""
caracteres = []

while entrada not in ["fin", "'fin'", "'fin", "fin'"]:
    caracteres.clear()
    caracter_invalido = 0

    entrada = input("Ingresa un número romano: ").strip().lower()

    if entrada not in ["fin", "'fin'", "'fin", "fin'"]:
        for i in entrada:
            caracteres.append(i)

        for i in range(len(caracteres)):
            if caracteres[i] not in ["i", "v", "x", "l", "c", "d", "m"]:
                caracter_invalido = 1
            else:
                if caracteres[i] == "i":
                    caracteres[i] = 1
                elif caracteres[i] == "v":
                    caracteres[i] = 5
                elif caracteres[i] == "x":
                    caracteres[i] = 10
                elif caracteres[i] == "l":
                    caracteres[i] = 50
                elif caracteres[i] == "c":
                    caracteres[i] = 100
                elif caracteres[i] == "d":
                    caracteres[i] = 500
                elif caracteres[i] == "m":
                    caracteres[i] = 1000

        if caracter_invalido == 1:
            print("No ha ingresado un número romano.")
        else:
            print(caracteres)

print("Fin del programa.")