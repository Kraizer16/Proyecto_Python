from Persistencia_Datos.Persistencia import guardar, cargar
from Modelo.lecturas import *
from datetime import datetime, timedelta

def registrarAsisSalida(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**5. Registro de Asistencia ***")
    
    codMod = leerCodigoMod()  # Leer código del módulo
    if codMod in lib["Modulos"]:
        cod = leerCodigo()  # Leer código del estudiante
        if cod in lib["Modulos"][codMod]["Integrantes"]:
            
            # Si no existe la clave 'Asistencia', la creamos
            if "Asistencia" not in lib["Modulos"][codMod]:
                lib["Modulos"][codMod]["Asistencia"] = {}

            # Leer fecha de la clase
            fecha = leerFecha()
            
            # Verificar si la fecha está registrada en 'Asistencia'
            if fecha not in lib["Modulos"][codMod]["Asistencia"]:
                print(f"No se ha registrado asistencia para el estudiante {cod} en la fecha {fecha}.")
                input("Presione cualquier tecla para volver al menú...")
                return lib
            
            # Verificar si el estudiante ha registrado la hora de llegada
            if cod not in lib["Modulos"][codMod]["Asistencia"][fecha]:
                print(">>> No se ha registrado la hora de llegada para el día de hoy <<<")
                input("Presione cualquier tecla para volver al menú...")
                return lib
            
            # Verificar si ya se ha registrado la hora de salida
            if "Hora de Salida" in lib["Modulos"][codMod]["Asistencia"][fecha][cod]:
                print(">>> Ya has registrado tu hora de salida para el día de hoy <<<")
                input("Presione cualquier tecla para volver al menú...")
                return lib

            # Leer hora de salida
            horaS = leerHora()
            
            # Asignar la hora de salida bajo la clave de la fecha
            lib["Modulos"][codMod]["Asistencia"][fecha][cod]["Hora de Salida"] = horaS

            # Guardar los cambios en el archivo JSON
            guardar(lib, arch)

            print(f"Hora de salida registrada exitosamente para el estudiante {cod} en el módulo {codMod}.")
        else:
            print(f"El código de estudiante {cod} no está inscrito en el módulo {codMod}.")
    else:
        print(f"El código de módulo {codMod} no existe en la base de datos.")

    input("Presione cualquier tecla para volver al menú...")
    return lib


def registrarAsisLlegada(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**5. Registro de Asistencia ***")
    
    codMod = leerCodigoMod()  # Leer código del módulo
    if codMod in lib["Modulos"]:
        cod = leerCodigo()  # Leer código del estudiante
        if cod in lib["Modulos"][codMod]["Integrantes"]:
            
            # Si no existe la clave 'Asistencia', la creamos
            if "Asistencia" not in lib["Modulos"][codMod]:
                lib["Modulos"][codMod]["Asistencia"] = {}

            # Leer fecha de la clase
            fecha = leerFecha()
            
            # Si no existe la fecha en 'Asistencia', la añadimos
            if fecha not in lib["Modulos"][codMod]["Asistencia"]:
                lib["Modulos"][codMod]["Asistencia"][fecha] = {}

            # Verificar si el estudiante ya ha registrado asistencia para el día
            if cod in lib["Modulos"][codMod]["Asistencia"][fecha]:
                print(">>> Ya has registrado asistencia el día de hoy <<<")
                input("Presione cualquier tecla para volver al menú...")
                return lib

            # Leer hora de entrada
            horaE = leerHora()

            # Asignar los datos de la asistencia bajo la clave de la fecha
            lib["Modulos"][codMod]["Asistencia"][fecha][cod] = {}
            lib["Modulos"][codMod]["Asistencia"][fecha][cod]["Hora de Llegada"] = horaE

            # Guardar los cambios en el archivo JSON
            guardar(lib, arch)

            print(">>> Asistencia registrada correctamente <<<")
        else:
            print(f"El código de estudiante {cod} no está inscrito en el módulo {codMod}.")
    else:
        print(f"El código de módulo {codMod} no existe en la base de datos.")

    input("Presione cualquier tecla para volver al menú...")
    return lib


def asignarGrupo(lib):

    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    Grupo = list(lib["Grupos"].keys())
    return Grupo


def insertDocAsigEst(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**4. INSERTAR Docente ***")
    
    # Si no existe la clave "Docentes", la creamos
    if "Docentes" not in lib:
        lib["Docentes"] = {}

    # Cantidad de Docentes que el usuario quiere registrar
    cantDocen = eleccion("Cuantos Docentes desea Registrar?\n\n(Puedes Registrar un maximo de 10 Docentes a la vez):\n\n")

    for i in range(cantDocen):
        # Leer Cédula de Docentes en cada iteración
        cedula = leerCedul()

        # Verificar si la cedula ya existe
        if cedula not in lib['Docentes']:
            # Si no existe, registrar el nuevo docente
            nombre = nomDocen()  # Función para leer el nombre del Docente
            
            Data = {
                "Nombre": nombre,
                "Estudiantes_Asignados": 0  # Número de estudiantes asignados
            }
            
            lib["Docentes"][cedula] = Data  # Insertar datos en el diccionario
            guardar(lib, arch)

            print("El instituto Acme Education tiene disponibles los siguientes modulos:")

            for k in lib["Modulos"].keys():
               print("\n" "Codigo : ", k, ":", lib["Modulos"][k]["Nombre"], end=" - ")

            cantDocImp = eleccionGt("\nA cuantos Modulos desea Impartir(min: 1 -- max: 3)\n")

            for i in range(cantDocImp):
                sw = True
                while sw:
                    mod = input("Escriba el codigo del modulo al que desea impartir\n").strip()
                    if mod not in lib["Modulos"].keys():
                        print("Error. Ingrese un codigo Valido")  
                        input("Presione cualquier tecla para continuar")
                    else:
                        # Asignar al docente en el módulo correspondiente
                        if "Docente/s" not in lib["Modulos"][mod]:
                            lib["Modulos"][mod]["Docente/s"] = {}

                        lib["Modulos"][mod]["Docente/s"][cedula] = {
                            "Nombre": lib["Docentes"][cedula]["Nombre"],
                            "Estudiantes_Asignados": 0  # Inicialmente ningún estudiante asignado
                        }
                        guardar(lib, arch)
                        print("Has sido registrado correctamente para impartir en el modulo ", lib["Modulos"][mod]["Nombre"])
                        sw = False
        else:
            # Si la cédula ya existe, imprimir mensaje
            print(f"El código {cedula} ya existe en la Base de datos.")
        guardar(lib, arch)  # Guardar los cambios en el archivo JSON

    # Asignar estudiantes a los docentes
    for mod in lib["Modulos"].keys():
        # Verificar si el módulo tiene docentes registrados y estudiantes para asignar
        if "Docente/s" in lib["Modulos"][mod] and "Integrantes" in lib["Modulos"][mod]:
            estudiantes = list(lib["Modulos"][mod]["Integrantes"].keys())  # Lista de estudiantes
            docentes = list(lib["Modulos"][mod]["Docente/s"].keys())  # Lista de docentes

            estudiante_idx = 0  # índice para recorrer los estudiantes
            docente_idx = 0  # índice para recorrer los docentes

            # Mientras haya estudiantes por asignar y docentes disponibles
            while estudiante_idx < len(estudiantes) and docente_idx < len(docentes):
                docente_actual = docentes[docente_idx]
                num_estudiantes_asignados = lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados"]

                # Verificar si el docente tiene menos de 20 estudiantes asignados
                if num_estudiantes_asignados < 20:
                    estudiante = estudiantes[estudiante_idx]

                    # Verificar si el estudiante ya está asignado
                    if "Estudiantes_Asignados_List" not in lib["Modulos"][mod]["Docente/s"][docente_actual]:
                        lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados_List"] = []
                    
                    # Solo agregar si el estudiante no está ya asignado
                    if estudiante not in lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados_List"]:
                        lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados_List"].append(estudiante)
                        lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados"] += 1
                        lib["Docentes"][cedula]["Estudiantes_Asignados"] = lib["Modulos"][mod]["Docente/s"][docente_actual]["Estudiantes_Asignados"]
                        estudiante_idx += 1  # Pasar al siguiente estudiante
                    else:
                        estudiante_idx += 1  # Pasar al siguiente estudiante si ya está asignado
                else:
                    # Si el docente ya tiene 20 estudiantes, pasar al siguiente docente
                    docente_idx += 1
                    # Verificar si se alcanzó el límite de docentes
                    if docente_idx >= len(docentes):
                        print(f"Todos los docentes del módulo '{mod}' han alcanzado el límite de estudiantes.")
                        break  # Salir del ciclo si ya no quedan docentes disponibles

            guardar(lib, arch)  # Guardar los cambios

    print("Asignación de estudiantes a docentes completada.")

    input("Presione cualquier tecla para volver al menú...")
    return lib






# def insertarDocentes(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**4. INSERTAR Docente ***")
    
    # Si no existe la clave "Docentes", la creamos
    if "Docentes" not in lib:
        lib["Docentes"] = {}

    # Cantidad de Docentes que el usuario quiere registrar
    cantDocen = eleccion("Cuantos Docentes desea Registrar?\n\n(Puedes Registrar un maximo de 10 Docentes a la vez):\n\n")

    for i in range(cantDocen):
        # Leer Cédula de Docentes en cada iteración
        cedula = leerCedul()

        # Verificar si la cedula ya existe
        if cedula not in lib['Docentes']:
            # Si no existe, registrar el nuevo Grupo
            nombre = nomDocen()  # Función para leer el nombre del Docente
            
            Data = {
                "Nombre": nombre,
            }
            
            lib["Docentes"][cedula] = Data  # Insertar datos en el diccionario
            guardar(lib, arch)

            print("A cual o cuales de los siguientes modulos Impartirá:")

            for k in lib["Modulos"].keys():
               print("\n", k,":",lib["Modulos"][k]["Nombre"], end = " - ")

            cantDocImp = eleccionGt("\nA cuantos Modulos desea Impartir(min: 1 -- max: 3)\n")

            for i in range(cantDocImp): 
                sw = True
                while sw:
                    mod = input("Escriba el codigo del modulo al que desea impartir\n").strip()
                    if mod not in lib["Modulos"].keys():
                        print("Error. Ingrese un codigo Valido")  
                        input("Presione cualquier tecla para continuar") 
                    for k in lib["Modulos"].keys():
                        
                        if mod == k:
                            if "Docente/s" not in lib["Modulos"][k]:

                             lib["Modulos"][k]["Docente/s"] = {}

                            lib["Modulos"][k]["Docente/s"][cedula] = lib["Docentes"][cedula]["Nombre"]
                            guardar(lib, arch)
                            print("Has sido registrado correctamente para impartir en el modulo ", lib["Modulos"][k]["Nombre"])

                            sw = False
           
        else:
          # Si la cédula ya existe, imprimir mensaje
          print(f"El código {cedula} ya existe en la Base de datos.")
        guardar(lib, arch)  # Guardar los cambios en el archivo JSON
    
    input("Presione cualquier tecla para volver al menu...")
    return lib


def insertarGrup(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**1. INSERTAR GRUPO ***")
    
    # Si no existe la clave "Grupo", la creamos
    if "Grupos" not in lib:
        lib["Grupos"] = {}

    # Cantidad de Grupos que el usuario quiere registrar
    cantGrup = eleccion("\nCuantos Grupos desea Registrar?\n\n(Puedes Registrar un maximo de 10 Grupos a la vez):\n\n")


    for i in range(cantGrup):
        # Leer código de módulo en cada iteración
        codGrup = leerCodigoGrup()

        # Verificar si el código ya existe
        if codGrup not in lib['Grupos']:
            # Si no existe, registrar el nuevo Grupo
            nombre = nomGrup()  # Función para leer el nombre del Grupo
            sigla = siglaGrup()  # Función para leer la Sigla del Grupo
            
            
            Data = {
                "Nombre": nombre,
                "Sigla ": sigla,
            }
            
            lib["Grupos"][codGrup] = Data  # Insertar datos en el diccionario

            guardar(lib, arch)  # Guardar los cambios en el archivo JSON
        
        else:
            # Si el código ya existe, imprimir mensaje
            print(f"El código {codGrup} ya existe en la Base de datos.")
    
    input("Presione cualquier tecla para volver al menu...")
    return lib


def insertarMod(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**2. INSERTAR MODULO ***")
    
    # Si no existe la clave "Modulos", la creamos
    if "Modulos" not in lib:
        lib["Modulos"] = {}

    # Cantidad de módulos que el usuario quiere registrar
    cantMod = eleccion("Cuantos Modulos desea Registrar?\n\n(Puedes Registrar un maximo de 10 Modulos a la vez):\n\n")

    for i in range(cantMod):
        # Leer código de módulo en cada iteración
        codMod = leerCodigoMod()

        # Verificar si el código ya existe
        if codMod not in lib['Modulos']:
            # Si no existe, registrar el nuevo módulo
            nombre = nomMod()  # Función para leer el nombre del módulo
            durSem = duraSem()  # Función para leer la duración en semanas del módulo
            
            # Leer la fecha de inicio
            while True:
                try:
                    fecha_inicio_str = input("Ingrese la fecha de inicio del módulo (formato: DD/MM/AAAA): ")
                    fecha_inicio = datetime.strptime(fecha_inicio_str, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Fecha inválida. Por favor ingrese el formato correcto (DD/MM/AAAA).")
            
            # Calcular la fecha de finalización en función de la duración en semanas
            fecha_fin = fecha_inicio + timedelta(weeks=durSem)
            fecha_fin_str = fecha_fin.strftime("%d/%m/%Y")

            # Leer la hora de inicio y fin de cada clase
            while True:
                try:
                    hora_inicio = input("Ingrese la hora de inicio de las clases (formato: HH:MM, 24 horas): ")
                    datetime.strptime(hora_inicio, "%H:%M")  # Validación del formato de hora
                    break
                except ValueError:
                    print("Hora inválida. Por favor ingrese el formato correcto (HH:MM).")
            
            while True:
                try:
                    hora_fin = input("Ingrese la hora de finalización de las clases (formato: HH:MM, 24 horas): ")
                    datetime.strptime(hora_fin, "%H:%M")  # Validación del formato de hora
                    break
                except ValueError:
                    print("Hora inválida. Por favor ingrese el formato correcto (HH:MM).")

            # Guardar los datos en el diccionario
            Data = {
                "Nombre": nombre,
                "Duracion Semanas": durSem,
                "Fecha Inicio": fecha_inicio_str,
                "Fecha Fin": fecha_fin_str,
                "Hora Inicio": hora_inicio,
                "Hora Fin": hora_fin
            }

            lib["Modulos"][codMod] = Data  # Insertar los datos en el diccionario
            guardar(lib, arch)  # Guardar los cambios en el archivo JSON
        else:
            # Si el código ya existe, imprimir mensaje
            print(f"El código {codMod} ya existe en la Base de datos.")
    
    input("Presione cualquier tecla para volver al menú...")
    return lib


def insertarEst(lib, arch):
    pos = 0  # Índice del grupo actual
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    print("\n\n**3. INSERTAR ESTUDIANTES ***".center(40))

    # Si no existe la clave 'Estudiantes', la creamos
    if "Estudiantes" not in lib:
        lib["Estudiantes"] = {}

    # Cantidad de estudiantes que el usuario quiere registrar
    cantEstudiantes = eleccion("Cuantos Estudi@ntes desea Registrar?\n\n(Puedes Registrar un maximo de 10 Estudi@ntes a la vez):\n\n")

    grupoAsig = list(lib["Grupos"].keys())  # Obtener la lista de grupos

    for i in range(cantEstudiantes):
        # Leer código del estudiante en cada iteración
        cod = leerCodigo()

        # Verificar si el código ya existe
        if cod not in lib['Estudiantes']:
            # Si no existe, registrar el nuevo estudiante
            nombre = nomEst()  # Función para leer el nombre del estudiante
            sexo = leerSexo()  # Función para leer el sexo del estudiante
            edad = leerEdad()  # Función para leer la edad del estudiante
            Data = {
                "Nombre": nombre,
                "Sexo": sexo,
                "edad": edad,
            }

            lib["Estudiantes"][cod] = Data  # Insertar datos en el diccionario
            guardar(lib, arch)

            # Verificar que el grupo actual no haya superado el límite de 5 estudiantes
            while len(lib["Grupos"][grupoAsig[pos]].get("cod_Integrantes", [])) >= 5:
                pos += 1  # Pasar al siguiente grupo

                # Si no hay más grupos disponibles, lanzar un error
                if pos >= len(grupoAsig):
                    print("No hay más grupos disponibles.")
                    return lib

            # Añadir el estudiante al grupo asignado
            if "Integrantes" not in lib["Grupos"][grupoAsig[pos]]:
                lib["Grupos"][grupoAsig[pos]]["Integrantes"] = {}

            lib["Grupos"][grupoAsig[pos]]["Integrantes"][cod] = lib["Estudiantes"][cod]["Nombre"]

            # Si 'cod_Integrantes' no existe, crear la lista
            if "cod_Integrantes" not in lib["Grupos"][grupoAsig[pos]]:
                lib["Grupos"][grupoAsig[pos]]["cod_Integrantes"] = []

            # Añadir el código del estudiante a 'cod_Integrantes'
            lib["Grupos"][grupoAsig[pos]]["cod_Integrantes"].append(cod)

            # Actualizar el número de estudiantes en 'num_Integrantes'
            lib["Grupos"][grupoAsig[pos]]["num_Integrantes"] = len(lib["Grupos"][grupoAsig[pos]]["cod_Integrantes"])

            print("\n>>> FELICITACIONES <<<\n".center(40))
            print(f"El estudiante {cod}: {lib['Estudiantes'][cod]['Nombre']} ha sido ingresado al grupo: {grupoAsig[pos]}\n")

            # Guardar los cambios en el archivo
            guardar(lib, arch)

            # Asignar estudiante a un docente
            for mod in lib["Modulos"].keys():
                if "Docente/s" in lib["Modulos"][mod]:  # Verificar si hay docentes en el módulo
                    docentes = list(lib["Modulos"][mod]["Docente/s"].keys())  # Lista de docentes

                    # Asignar al estudiante a un docente disponible
                    for docente in docentes:
                        num_estudiantes_asignados = lib["Modulos"][mod]["Docente/s"][docente]["Estudiantes_Asignados"]

                        if num_estudiantes_asignados < 20:  # Verificar límite de estudiantes por docente
                            if "Estudiantes_Asignados_List" not in lib["Modulos"][mod]["Docente/s"][docente]:
                                lib["Modulos"][mod]["Docente/s"][docente]["Estudiantes_Asignados_List"] = []

                            # Verificar si el estudiante ya está asignado
                            if cod not in lib["Modulos"][mod]["Docente/s"][docente]["Estudiantes_Asignados_List"]:
                                lib["Modulos"][mod]["Docente/s"][docente]["Estudiantes_Asignados_List"].append(cod)
                                lib["Modulos"][mod]["Docente/s"][docente]["Estudiantes_Asignados"] += 1
                                lib["Docentes"][cedula]["Estudiantes_Asignados"] += 1

                                print(f"El estudiante {cod} ha sido asignado al docente {docente}.")
                                break  # Salir del ciclo una vez que se asigne el estudiante

            # Registro en módulos
            print("El instituto ofrece los siguientes Modulos:")
            for k in lib["Modulos"].keys():
                print("\n", k, ":", lib["Modulos"][k]["Nombre"], end=" - " "\n")

            cantModEstu = eleccionGt("\nA cuantos modulos desea registrarse(min: 1 -- max: 3)\n")

            for i in range(cantModEstu): 
                sw = True
                while sw:
                    mod = input("\nEscriba el codigo del modulo\n").strip()
                    if mod not in lib["Modulos"].keys():
                        print("Error. Ingrese un codigo Valido")  
                        input("Presione cualquier tecla para continuar") 
                    for k in lib["Modulos"].keys():
                        if mod == k:
                            if "Integrantes" not in lib["Modulos"][k]:
                                lib["Modulos"][k]["Integrantes"] = {}

                            lib["Modulos"][k]["Integrantes"][cod] = lib["Estudiantes"][cod]["Nombre"]
                            guardar(lib, arch)
                            print(">>> Has sido registrado correctamente en el modulo ", lib["Modulos"][k]["Nombre"], " <<<\n")
                            sw = False
            
            guardar(lib, arch)
        else:
            # Si el código ya existe, imprimir mensaje
            print(f"El código {cod} ya existe en la Base de datos.")
    
    input("\nPresione cualquier tecla para volver al menú...")
    return lib


def consultarGroup(lib):
    print("\n\n**1. Estudiantes Matriculados en un grupo ***\n")
    print("Los grupos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Grupos"].keys():
        print("Codigo:", k, ">>>>  Nombre:", lib["Grupos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el codigo del Grupo Al que desea Consultar sus estudiantes Matriculados\n\nCod >> ")

    if cod in lib["Grupos"]:
        if "Integrantes" in lib["Grupos"][cod]:
            print("\nLos estudiantes matriculados en el Grupo:\nCodigo:", cod, ">>>>  Nombre:", lib["Grupos"][cod]["Nombre"], " son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Codigo del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes del grupo e imprimirlos en formato de tabla
            for c, nombre in lib["Grupos"][cod]["Integrantes"].items():
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nEl Grupo: {cod} con el Nombre: {lib['Grupos'][cod]['Nombre']} No tiene Estudiantes Matriculados")
    else:
        print(">>> Error. El codigo del Grupo no existe en AcmeEducation")

    input("\nPresione cualquier tecla para volver al menu...")


def consultarMod(lib):
    print("\n\n**2. Estudiantes Matriculados en un Modulo ***\n")
    print("Los Modulos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Modulos"].keys():
        print("Codigo:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el codigo del modulo al que desea consultar sus estudiantes matriculados\n\nCod >> ")

    if cod in lib["Modulos"]:
        if "Integrantes" in lib["Modulos"][cod]:
            print("\nLos estudiantes matriculados en el Modulo:\nCodigo:", cod, ">>>>  Nombre:", lib["Modulos"][cod]["Nombre"], " son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Codigo del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes del grupo e imprimirlos en formato de tabla
            for c, nombre in lib["Modulos"][cod]["Integrantes"].items():
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nEl Modulos: {cod} con el Nombre: {lib['Modulos'][cod]['Nombre']} No tiene Estudiantes Matriculados")
    else:
        print(">>> Error. El codigo del Grupo no existe en AcmeEducation")

    input("\nPresione cualquier tecla para volver al menu...")


def consultarDoc(lib):
    print("\n\n**3. Docentes que imparten en un Modulo ***\n")
    print("Los Modulos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Modulos"].keys():
        print("Codigo:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el codigo del modulo al que desea consultar los docentes que imaprten\n\nCod >> ")

    if cod in lib["Modulos"]:
        if "Docente/s" in lib["Modulos"][cod]:
            print("\nLos docentes que imparten en el Modulo:\nCodigo:", cod, ">>>>  Nombre:", lib["Modulos"][cod]["Nombre"], " son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Cedula del Docente':<30} {'Nombre del Docente':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes del grupo e imprimirlos en formato de tabla
            for c in lib["Modulos"][cod]["Docente/s"].keys():
                nombre = lib["Modulos"][cod]["Docente/s"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nEl Modulos: {cod} con el Nombre: {lib['Modulos'][cod]['Nombre']} No tienen Docentes que imparten")
    else:
        print(">>> Error. El codigo del Grupo no existe en AcmeEducation")

    input("\nPresione cualquier tecla para volver al menu...")


def consultarDocImpar(lib):
    print("\n\n**4. Consultar los estudiantes a cargo de un docente en un módulo ***\n")
    print("Los Modulos registrados en AcmeEducation son los siguientes: \n")
    
    # Mostrar los módulos disponibles
    for k in lib["Modulos"].keys():
        print("Codigo:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el codigo del modulo al que desea consultar los Estudiantes a cargo de un docente\n\nCod >> ")

    # Verificar si el módulo existe
    if cod in lib["Modulos"]:
        # Verificar si hay docentes en el módulo
        if "Docente/s" in lib["Modulos"][cod]:
            print("\nLos docente/s que imparten en el Modulo :\nCodigo:", cod, ">>>>  Nombre:", lib["Modulos"][cod]["Nombre"], " son:\n")
            
            # Imprimir encabezados
            print(f"{'Cedula del Docente':<30} {'Nombre del Docente':<40}")
            print("=" * 50)
            
            # Mostrar la lista de docentes del módulo
            for c in lib["Modulos"][cod]["Docente/s"].keys():
                nombre = lib["Modulos"][cod]["Docente/s"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
            
            # Ciclo para elegir un docente y mostrar los estudiantes a su cargo
            sw = True
            while sw:
                try:
                    codDoc = input("\nIngrese la cedula del docente que desea saber cuales estudiantes tiene a cargo\nCedula >>> ")
                    # Verificar si el docente está en el módulo
                    if codDoc in lib["Modulos"][cod]["Docente/s"]:
                        print("\nEl docente", lib["Modulos"][cod]["Docente/s"][codDoc]["Nombre"], "está a cargo de los siguientes estudiantes:\n")
                        
                        print(f"{'Codigo del Estudiante':<30} {'Nombre del Estudiante':<40}")
                        print("=" * 50)
                        
                        # Iterar sobre la lista de estudiantes asignados al docente
                        estudiantes_asignados = lib["Modulos"][cod]["Docente/s"][codDoc]["Estudiantes_Asignados_List"]
                        for estudiante_cod in estudiantes_asignados:
                            nombre = lib["Estudiantes"][estudiante_cod]["Nombre"]
                            print(f"{estudiante_cod:<30} {nombre:<40}")
                        
                        sw = False  # Terminar el ciclo al mostrar la lista
                    else:
                        print(f"El docente con cédula {codDoc} no está asignado a este módulo.")
                except Exception as e:
                    print("Error: ", e)
        else:
            print(f"\nEl módulo: {cod} con el nombre: {lib['Modulos'][cod]['Nombre']} no tiene docentes asignados.")
    else:
        print(">>> Error: El código del módulo no existe en AcmeEducation.")

    input("\nPresione cualquier tecla para volver al menú...")


def consultarEstudiantesTarde(lib):
    print("\n\n**1. Estudiantes que llegaron tarde a un Módulo ***\n")
    print("Los Módulos registrados en AcmeEducation son los siguientes: \n")
    # lib = "Proyecto/acmeEducation.json"
    for k in lib["Modulos"].keys():
        print("Código:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el código del módulo al que desea consultar los estudiantes que llegaron tarde\n\nCod >> ")

    if cod in lib["Modulos"]:
        # Verificar si hay informes de estudiantes que llegaron tarde
        if "Informes" in lib["Modulos"][cod] and "EstudiantesTarde" in lib["Modulos"][cod]["Informes"]:
            tarde_estudiantes = lib["Modulos"][cod]["Informes"]["EstudiantesTarde"]
            print(f"\nLos estudiantes que llegaron tarde al Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes que llegaron tarde e imprimirlos en formato de tabla
            for c in tarde_estudiantes:
                nombre = lib["Estudiantes"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nNo hay un informe de estudiantes que llegaron tarde al Módulo: {cod}. Creando informe...\n")
            mes_especifico = input("Ingrese el mes para el cual desea generar el informe (ejemplo: 09 para septiembre): ")
            estudiantes_llegaron_tarde(lib, cod, mes_especifico)
            tarde_estudiantes = lib["Modulos"][cod]["Informes"]["EstudiantesTarde"]
            print(f"\nLos estudiantes que llegaron tarde al Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes que llegaron tarde e imprimirlos en formato de tabla
            for c in tarde_estudiantes:
                nombre = lib["Estudiantes"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
    else:
        print(">>> Error. El código del Módulo no existe en AcmeEducation.")

    input("\nPresione cualquier tecla para volver al menú...")


def consultarEstudiantesRetiradosAntes(lib):
    print("\n\n**1. Estudiantes que se retiraron antes de finalizar una sesión ***\n")
    print("Los Módulos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Modulos"].keys():
        print("Código:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el código del módulo al que desea consultar los estudiantes que se retiraron antes de finalizar la sesión\n\nCod >> ")

    if cod in lib["Modulos"]:

        # Verificar si hay informes de estudiantes que se retiraron antes
        if "Informes" in lib["Modulos"][cod] and "EstudiantesRetiradosAntes" in lib["Modulos"][cod]["Informes"]:
            retirados_estudiantes = lib["Modulos"][cod]["Informes"]["EstudiantesRetiradosAntes"]
            print(f"\nLos estudiantes que se retiraron antes de finalizar la sesión del Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes que se retiraron antes e imprimirlos en formato de tabla
            for c in retirados_estudiantes:
                nombre = lib["Estudiantes"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nNo hay un informe de estudiantes que se retiraron antes de finalizar la sesión del Módulo: {cod}. Creando informe...\n")
            mes_especifico = input("Ingrese el mes para el cual desea generar el informe (ejemplo: 09 para septiembre): ")
            estudiantes_se_retiraron_antes(lib, cod, mes_especifico)
            retirados_estudiantes = lib["Modulos"][cod]["Informes"]["EstudiantesRetiradosAntes"]
            print(f"\nLos estudiantes que se retiraron antes de finalizar la sesión del Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes que se retiraron antes e imprimirlos en formato de tabla
            for c in retirados_estudiantes:
                nombre = lib["Estudiantes"][c]["Nombre"]
                print(f"{c:<30} {nombre:<40}")
    else:
        print(">>> Error. El código del Módulo no existe en AcmeEducation.")

    input("\nPresione cualquier tecla para volver al menú...")


def consultarEstudiantesSinFaltas(lib):
    print("\n\n**3. Estudiantes que no han faltado a ningún Módulo durante un mes específico ***\n")
    print("Los Módulos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Modulos"].keys():
        print("Código:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el código del módulo al que desea consultar los estudiantes sin faltas\n\nCod >> ")

    if cod in lib["Modulos"]:
        # Verificar si hay informes de estudiantes sin faltas
        if "Informes" in lib["Modulos"][cod] and "EstudiantesSinFaltas" in lib["Modulos"][cod]["Informes"]:
            sin_faltas_estudiantes = lib["Modulos"][cod]["Informes"]["EstudiantesSinFaltas"]
            print(f"\nLos estudiantes que no han faltado a ningún Módulo durante el mes en el Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
            
            # Imprimir una tabla con encabezados
            print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
            print("=" * 50)
            
            # Iterar sobre los estudiantes que no han faltado e imprimirlos en formato de tabla
            for c in sin_faltas_estudiantes:
                nombre = lib["Estudiantes"].get(c, {}).get("Nombre", "Desconocido")  # Manejo de errores
                print(f"{c:<30} {nombre:<40}")
        else:
            print(f"\nNo hay un informe de estudiantes que no han faltado al Módulo: {cod}. Creando informe...\n")
            mes_especifico = input("Ingrese el mes para el cual desea generar el informe (ejemplo: 09 para septiembre): ")
            estudiantes_sin_faltas(lib, cod, mes_especifico)  # Llama la función para crear el informe

            # Verificar nuevamente el informe después de crear uno
            sin_faltas_estudiantes = lib["Modulos"][cod]["Informes"].get("EstudiantesSinFaltas", [])
            if sin_faltas_estudiantes:
                print(f"\nLos estudiantes que no han faltado a ningún Módulo durante el mes en el Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} son:\n")
                
                # Imprimir una tabla con encabezados
                print(f"{'Código del Estudiante':<30} {'Nombre del Estudiante':<40}")
                print("=" * 50)
                
                # Iterar sobre los estudiantes que no han faltado e imprimirlos en formato de tabla
                for c in sin_faltas_estudiantes:
                    nombre = lib["Estudiantes"].get(c, {}).get("Nombre", "Desconocido")  # Manejo de errores
                    print(f"{c:<30} {nombre:<40}")
            else:
                print(f"No se encontraron estudiantes sin faltas para el mes especificado en el Módulo: {cod}.")
    else:
        print(">>> Error. El código del Módulo no existe en AcmeEducation.")

    input("\nPresione cualquier tecla para volver al menú...")


def consultarPorcentajeAsistencia(lib): 
    print("\n\n**3. Porcentaje de Asistencia por Módulo ***\n")
    print("Los Módulos registrados en AcmeEducation son los siguientes: \n")
    
    for k in lib["Modulos"].keys():
        print("Código:", k, ">>>>  Nombre:", lib["Modulos"][k]["Nombre"], end=" - \n")

    cod = input("\nIngrese el código del módulo para consultar el porcentaje de asistencia\n\nCod >> ")

    if cod in lib["Modulos"]:
        # Verificar si hay informes de porcentaje de asistencia
        if "Informes" in lib["Modulos"][cod] and "PorcentajeAsistencia" in lib["Modulos"][cod]["Informes"]:
            porcentaje_asistencia = lib["Modulos"][cod]["Informes"]["PorcentajeAsistencia"]
            print(f"\nEl porcentaje de asistencia en el Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} es: {porcentaje_asistencia:.2f}%")
        else:
            print(f"\nNo hay un informe de porcentaje de asistencia para el Módulo: {cod}. Creando informe...\n")
            mes_especifico = input("Ingrese el mes para el cual desea generar el informe (ejemplo: 09 para septiembre): ")
            porcentaje_asistencia = porcentaje_asistencia_por_modulo(lib, cod, mes_especifico)
            print(f"\nEl porcentaje de asistencia en el Módulo:\nCódigo: {cod}  >>>>  Nombre: {lib['Modulos'][cod]['Nombre']} es: {porcentaje_asistencia:.2f}%")
    else:
        print(">>> Error. El código del Módulo no existe en AcmeEducation.")

    input("\nPresione cualquier tecla para volver al menú...")


def cambiarContra(lib, arch):
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    while True:
        try:
            Usuario = input((">>> INGRESE SU USUARIO <<<\nUSUARIO>>> "))
            if Usuario in lib["Usuario"]:
                password = input("\n>>> INGRESE SU NUEVA CONTRASEÑA <<<\nCONTRASEÑA>>> ")
                confirmar_pass = input("\n>>> CONFIRME SU NUEVA CONTRASEÑA <<<\nCONTRASEÑA>>> ")
                if password == confirmar_pass:
                    password = encriptar_contraseña(password)
                    data ={
                        "contrase": password
                    }
                    lib["Usuario"][Usuario] = data
                    guardar(lib, arch)
                    input("Presione cualquier tecla para volver al menu principal")
                return lib
            print(">>> Usuario Incorrecto <<<")
        except Exception as e:
            print(">>> ERROR. ", e)