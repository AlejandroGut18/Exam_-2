import pyodbc

def insertar(profesor, conexion):
    try:
        cursor = conexion.cursor()
        query = 'INSERT INTO Profesores VALUES(?, ?, ?, ?)'
        cursor.execute(query, profesor['id'], profesor['nombre'], profesor['apellido'], profesor['especialidad'])
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al insertar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None

def buscar(id, conexion):
    try:
        cursor = conexion.cursor()
        query = 'SELECT * FROM Profesores WHERE ProfesorID = ?'
        cursor.execute(query, id)
        resultado = cursor.fetchone()
        return resultado
    except pyodbc.Error as error:
        print(f'Error al buscar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None

def actualizar(id, conexion):
    try:
        resultado = buscar(id, conexion)
        if not resultado:
            print('Profesor no encontrado...')
            input('Presione Enter para continuar...')
            return None
        print('===PROFESOR===')
        print(f"ID: {id}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nEspecialidad: {resultado[3]}")
        print('Escoja campo a actualizar:\n1 - Nombre\n2 - Apellido\n3 - Especialidad\n4 - Todos los campos\n5 - Cancelar')
        r = input('Ingrese una opción: ')
        while True:
            if not r.isdigit():
                print("Por favor ingrese un numero valido")
                input("Presione enter para continuar...")
                continue
            else:
                break
        r = int(r)
        if r == 5:
            return
        cursor = conexion.cursor()
        match r:
            case 1:
                nombre = input('Ingrese nuevo nombre: ')
                query = 'UPDATE Profesores SET Nombre = ? WHERE ProfesorID = ?'
                cursor.execute(query, nombre, id)
            case 2:
                apellido = input('Ingrese nuevo Apellido: ')
                query = 'UPDATE Profesores SET Apellido = ? WHERE ProfesorID = ?'
                cursor.execute(query, apellido, id)
            case 3:
                especialidad = input('Ingrese nueva Especialidad: ')
                query = 'UPDATE Profesores SET Especialidad = ? WHERE ProfesorID = ?'
                cursor.execute(query, especialidad, id)
            case 4: 
                nombre = input('Ingrese nuevo nombre: ')
                apellido = input('Ingrese nuevo Apellido: ')
                especialidad = input('Ingrese nueva Especialidad: ')
                query = 'UPDATE Profesores SET Nombre = ?, Apellido = ?, Especialidad = ? WHERE ProfesorID = ?'
                cursor.execute(query, nombre, apellido, especialidad, id)
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al actualizar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def eliminar(id, conexion):
    try:
        resultado = buscar(id, conexion)
        if not resultado:
            print('Distribuidor no encontrado...')
            input('Presione Enter para continuar...')
            return None
        print('===PROFESOR===')
        print(f"ID: {id}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nEspecialidad: {resultado[3]}")
        print('Desea eliminarlo?:\n1 - Si\n2 - No')
        r = input('Ingrese una opción: ')
        while True:
            if not r.isdigit():
                print("Por favor ingrese un numero valido")
                input("Presione enter para continuar...")
                continue
            else:
                break
        r = int(r)
        match r:
            case 1:
                cursor = conexion.cursor()
                cursor.execute('DELETE FROM Profesores WHERE ProfesorID = ?', id)
                cursor.commit()
                cursor.close()
                return True
            case 2:
                return False
        
    except pyodbc.Error as error:
        print(f'Error al actualizar 💀💀💀. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    

def Listar(conexion):
    if not conexion:
        print('Saliendo... 😔😓')
        exit()
    cursor = conexion.cursor()
    cursor.execute("SELECT ProfesorID, Nombre, Apellido, Especialidad FROM Profesores")  
    data = cursor.fetchall()

    encabezados = ["ProfesorID", "Nombre", "Apellido", "Especialidad"]
    
    listaFinal = [encabezados] + [list(fila) for fila in data] 

    anchos_columnas = [max(len(str(item)) for item in col) for col 
                       in zip(*listaFinal)]
    #print(anchos_columnas)
    for fila in listaFinal:
        print(" | ".join(f'{str(item):<{anchos_columnas[i]}}' for i, item in enumerate(fila)))

def validarInput(message = None):
    while True:
        entrada = input(message)
        if not entrada.isdigit():
            print("Por favor ingrese un numero valido")
            input("Presione enter para continuar...")
            continue
        entrada = int(entrada)
        return entrada
        