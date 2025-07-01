"""
Este Gestor de notas permitirá :
- Crear nota
- Leer todas las notas
- Buscar por palabra clave
- Eliminar nota
- Guardar las notas en un archivo Notas.json
- Leer notas desde el archivo Notas.json
"""
import json

notas = []


def agregar_nota():
    print("\n=== Agregar Nota ===")
    
    while True:
        titulo = input("Titulo de la nota: ").strip()
        contenido = input("Contenido de la nota : ").strip()
        if not titulo or not contenido:
            print("El título o el contenido no pueden estar va")

        nota = {
            "titulo": titulo,
            "contenido": contenido
        }
        notas.append(nota)
        print("Nota agregada correctamente \n")
        break


def mostrar_notas():
    resultado = []
    for nota in notas:
        resultado.append((nota["titulo"], nota["contenido"]))
    return resultado
    

def buscar_en_notas():
    print("\n== Buscar en notas ==")
    palabra_clave = input("Introduce la palabra clave para buscar : ").strip().lower()

    notas_encontradas = []
    for nota in notas:
        if palabra_clave in nota["titulo"].lower() or palabra_clave in nota["contenido"].lower():
            notas_encontradas.append(nota)
        
    return notas_encontradas, palabra_clave


def eliminar_nota():
    print("\n == Eliminar Nota ==")
    titulo_a_eliminar = input("Ingresa el título de la nota que deseas eliminar: ").strip().lower()

    posibles_notas_a_eliminar = []

    for i, nota in enumerate(notas):
        print(i, nota)
        if titulo_a_eliminar == nota["titulo"].lower():
            posibles_notas_a_eliminar.append((i, nota))
    if not posibles_notas_a_eliminar:
        print(f'No se encontraron notas con el titulo {titulo_a_eliminar}.\n')
    elif len(posibles_notas_a_eliminar) == 1:
        indice_a_eliminar, nota_encontrada = posibles_notas_a_eliminar[0]
        print('\nSe encontró una nota:')
        print(f'Título: {nota_encontrada["titulo"]}')
        print("_____________________")
        print(f'Contenido: {nota["contenido"]}')
        confirmacion = input("Estas seguro que quieres eliminar esta nota? (s/n):").strip().lower()
        if confirmacion == "s":
            del notas[indice_a_eliminar]
            print("Nota eliminada correctamente. \n")
        else:
            print("Operación cancelada. \n")
    else:
        print(f"\nSe encontraron varias notas con el titulo '{titulo_a_eliminar}'")

        for j, (indice_original, nota_actual) in enumerate(posibles_notas_a_eliminar):
            print(f"{j+1}. Título: {nota_actual["titulo"]} - Contenido: {nota_actual["contenido"][:30]} ...")

        while True:
            try:
                seleccion = int(input("Ingresa el número  de la nota que deseas eliminar o 0 para Cancelar: "))
                if seleccion == 0:
                    print("Operación cancelada.\n")
                    break
                elif 1 <= seleccion <= len(posibles_notas_a_eliminar):
                    indice_en_notas_original = posibles_notas_a_eliminar[seleccion - 1][0]
                    del notas[indice_en_notas_original]
                    print("nota eliminada correctamente. \n")
                    break
                else:
                    print("Número invalido, por favor intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número nuevamente")


def guardar_en_archivo():
    nombre_archivo = "mis_notas.json"

    with open(nombre_archivo, "w") as archivo:
        json.dump(notas, archivo, indent=4)


def cargar_desde_archivo():
    nombre_archivo = "mis_notas.json"

    try:
        with open(nombre_archivo, "r") as archivo:
            pass
    except FileNotFoundError:
        print(f"Archivo '{nombre_archivo}' no encontrado. Se iniciará con notas vacias.")




def mostrar_menu():

    print("\n === Gestor de Notas === \n")
    print("1. Crear una nota")
    print("2. leer todas las notas")
    print("3. buscar por palabra clave")
    print("4. eliminar nota")
    print("5. Guardar notas en un archivo")
    print("6. Cargar notas desde un archivo.")
    print("7. Para salir")


while True:
    mostrar_menu()
    opcion = input("Ingresa una opcion: \n")
    
    if opcion == "1":
        agregar_nota()

    elif opcion == "2":

        notas_obtenidas = mostrar_notas()
        if not notas_obtenidas:
            print("No hay notas para mostrar aún.\n")
        else:
            for titulo, contenido in notas_obtenidas:
                print(f'Título: {titulo}')
                print('----------------')
                print(f'Contenido : {contenido}\n')

    elif opcion == "3":
        notas_encontradas, palabra_clave = buscar_en_notas()

        if not notas_encontradas: 
            print(f"No se encontraron Notas con la palabra {palabra_clave} en las notas")
        else:
            print(f"Notas encontradas para {palabra_clave}")
        for nota in notas_encontradas:
            print(f"Título: {nota["titulo"]}")
            print("-----------------------")
            print(f"Contenido: {nota["contenido"]}")

    elif opcion == "4":
        eliminar_nota()
    elif opcion == "5":
        guardar_en_archivo()
    elif opcion == "6":
        pass
    elif opcion == "7":
        print("Gracias por utilizar el Gestor de notas")
        break
    else:
        print("Opcion invalida, vuelve a intentarlo")