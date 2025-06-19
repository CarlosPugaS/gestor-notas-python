"""
Este Gestor de notas permitirá :
- Crear nota
- Leer todas las notas
- Buscar por palabra clave
- Eliminar nota
- Guardar en archivo
"""
notas = [{"titulo": "algo", "contenido": "algo"}]


def agregar_nota():
    print("\n=== Agregar Nota ===")
    titulo = input("Titulo de la nota: ").strip()
    contenido = input("Contenido de la nota : ").strip()

    nota = {
        "titulo": titulo,
        "contenido": contenido
    }
    notas.append(nota)
    print("Nota agregada correctamente \n")


def mostrar_notas():
    resultado = []
    for nota in notas:
        for titulo, contenido in nota.items():
            resultado.append((titulo, contenido))
    return resultado
    

def buscar_en_notas():
    pass


def eliminar_nota():
    pass


def guardar_en_archivo():
    pass


def mostrar_menu():

    print("\n === Gestor de Notas === \n")
    print("1. Crear una nota")
    print("2. leer todas las notas")
    print("3. buscar por palabra clave")
    print("4. eliminar nota")
    print("5. Guardar la nota en un archivo")
    print("6. Para salir")


while True:
    mostrar_menu()
    opcion = input("Ingresa una opcion: \n")
    
    if opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("Gracias por utilizar el Gestor de notas")
        break
    else:
        print("Opcion invalida, vuelve a intentarlo")