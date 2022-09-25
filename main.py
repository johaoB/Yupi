from dataclasses import dataclass

@dataclass
class Biblioteca:
    registro = []
    alquiler = []
    r= len(registro)
    a= len(alquiler)

class Usuario:
    nombre:str = ""
    dni:str = ""


def registrar_usuario():
    print()
    Usuario.nombre = input("Cual es tu nombre: ")
    Biblioteca.registro.append(Usuario.nombre)
    print()
    opc1 = input("""1.Tarjeta de Identidad (T.I.)
2.Cedula de ciudadania (C.C.)
        
Que tipo de Identificacion utiliza: """)

    if opc1 == "1":
        print()
        Usuario.dni = str(input("Tarjeta de identidad:"))
        Biblioteca.registro.append(Usuario.dni)

    elif opc1 == "2":
        print()
        Usuario.dni = str(input("Cedula de ciudadania:"))
        Biblioteca.registro.append(Usuario.dni)

    else:
        print()
        print("Opcion invalida")
        registrar_usuario()

class Estanterias:
    cantidad:int
    categoria:str


class Libros:
    codigo:str =["64","25"]
    nombre:str =["Don quijote", "La casa verde"]

def info_libro(self):
    print()
    libro = str(input("Que libro deseas?: "))
    indice = Libros.nombre.index(libro)
    if libro == Libros.nombre[indice]:
        print()
        print("Nombre:"+ Libros.nombre[indice]+ ", Codigo:"+ Libros.codigo[indice])

    else:
        print()
        print("Ese libro no esta en nuestro catalogo")

    usuario = str(input("Cual es su Usuario?: "))
    i = Biblioteca.registro.index(usuario)
    if usuario == Biblioteca.registro[i]:
        Biblioteca.alquiler.append(Biblioteca.registro[i])
        Biblioteca.alquiler.append(Libros.nombre[indice])
        Biblioteca.alquiler.append(Libros.codigo[indice])

    else:
        print()
        print("Este usuario no esta registrado")


def menu():
    print("1. Registrar un usuario")
    print("2. Alquilar libro")
    print("3.")
    print("4. Salir")

def main():
    print("Bienvenido a la Biblioteca virtual")
    while(1):
        menu()
        opc = input("Elija un opcion: ")
        print()

        if (opc == "1"):
            registrar_usuario()

        elif (opc == "2"):
            info_libro(1)

        elif (opc == "3"):
            print()

        elif (opc == "4"):
            break

        else:
            print()
            print("Error: opcion invalida")
    print()
    print("Gracias por usar nuestra Biblioteca virtual")

def database():
    print("Usuarios: ", Biblioteca.registro)
    print("Alquilaron: ", Biblioteca.alquiler)

main()
database()
