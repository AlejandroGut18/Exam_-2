from db.profesores import *
from db.connection import *
import os

SERVER = 'ALEJANDRO\SQLEXPRESS'
DATABASE = 'Escuela'
TABLE = 'Profesores'

def main():
    conexion = conectar(SERVER, DATABASE)

    while True:
        os.system('cls')
        print('=====MANTENIMIENTO=====')
        print(f'BASE DE DATOS: {DATABASE} | TABLA: {TABLE}')
        print('1 - Agregar un Profesor\n2 - Actualizar datos de Profesores\n3 - Buscar Profesores\n4 - Eliminar Profesores\n5 - Listar Profesores\n6 - Salir\n')
        
        r = validarInput(message='Ingrese una opción: ')

        if r == 6:
            break
        match r:
            case 1:
                os.system('cls')
                id = validarInput('Ingrese identificador (ID): ')
                result = buscar(id, conexion)
                if result!= None:
                    print(f'Este registro ya existe')
                    input("Presione enter para continuar...")
                    continue
                nombre = input('Ingrese nombre: ')
                apellido = input('Ingrese apellido: ')
                especialidad = input('Ingrese especialidad : ')
                prof = {
                    'id': id,
                    'nombre':nombre,
                    'apellido':apellido,
                    'especialidad':especialidad
                }
                result = insertar(prof, conexion)
                if(result):
                    print('Profesor registrado exitosamente! 💕💕💕')
                    input("Presione enter para continuar...")

            case 2:
                os.system('cls')
                id = validarInput('Ingrese identificador (ID): ')
                resultado = actualizar(id, conexion)
                if(resultado):
                    print('Profesor actualizado exitosamente! 💕💕💕')
                    input("Presione enter para continuar...")
            case 3:
                os.system('cls')
                id = validarInput('Ingrese identificador (ID): ')
                resultado = buscar(id, conexion)
                if resultado:
                    print('=== PROFESOR ===')
                    print(f"ID: {id}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nEspecialidad: {resultado[3]}")
                    input('Presione Enter para continuar...')
                else:
                    print('Profesor no encontrado...')
                    input('Presione Enter para continuar...')
            case 4:
                os.system('cls')
                id = validarInput('Ingrese identificador (ID): ')
                resultado = eliminar(id, conexion)
                if(resultado):
                    print('Profesor eliminado exitosamente! 💕💕💕')
                    input("Presione enter para continuar...")
            case 5:
                os.system('cls')
                Listar(conexion)
                input('Presione Enter para continuar...')
            


if __name__ == '__main__':
    main()

 