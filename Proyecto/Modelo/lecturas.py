from datetime import datetime, timedelta
from Persistencia_Datos.Persistencia import guardar, cargar
import hashlib


def eleccionGt(msg):
    while True:
        try:
            opcion = int(input(msg))
            if opcion < 1 or opcion > 3:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para continuar")
                continue
            return opcion
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para continuar")


def eleccion(msg):
    while True:
        try:
            opcion = int(input(msg))
            if opcion < 1 or opcion > 10:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para continuar")
                continue
            return opcion
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para continuar")


def leerHora():
    hora = datetime.now()
    horas, minutos = str(hora).split()[1].split(":")[:2]
    return f"{horas}:{minutos}"


def leerFecha():
 fecha = datetime.now()
 ano, mes, dia = str(fecha).split()[0].split("-")
 return f"{dia}/{mes}/{ano}"


def nomDocen():
     while True:
        try:
            name = input("¿Nombre del Docente? ")
            if len(name.strip()) == 0:
                print(">>>ERROR. El nombre es invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def leerCedul():
    while True:
        try:
            cedula = int(input("Cédula del docente: "))
            if cedula <= 0:
                print(">>> Error. Cédula inválida")
                continue
            return cedula
        except ValueError:
            print(">>>> Error. Cédula inválida")


def siglaGrup():
      while True:
        try:
            sigla = input("¿Sigla del grupo? (tres caracteres : (ABC))")
            if len(sigla.strip()) == 0 or len(sigla.strip()) > 3:
                print(">>>ERROR. La sigla es invalida")
                continue
            return sigla
        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def duraSem():
    while True:
        try:
            durMod = int(input("Duración del Modulo: "))
            if durMod <= 0:
                print(">>> Error. Duracion inválida")
                continue
            return durMod
        except ValueError:
            print(">>>> Error. Duracion inválida")


def leerEdad():
    while True:
        try:
            edad = int(input("Edad del Estudiante: "))
            if edad <= 0:
                print(">>> Error. Edad inválida")
                continue
            return edad
        except ValueError:
            print(">>>> Error. Edad inválida")


def leerSexo():
     while True:
        try:
            sexo = input("¿Sexo del estudiante? (M o F) (M = Masculino) (F = Femenino) ")
            if sexo == "m" or sexo == "M" or sexo == "f" or sexo == "F":
                return sexo
            elif sexo != "m" or sexo != "M" or sexo != "f" or sexo != "F":
                print(">>>ERROR. El sexo ingresado es inválido")
                continue
                
        except Exception as e:
            print("Error al ingresar el Sexo.\n" + e)


def nomGrup():
     while True:
        try:
            name = input("¿Nombre del Grupo? ")
            if len(name.strip()) == 0:
                print(">>>ERROR. El nombre es invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def nomMod():
     while True:
        try:
            name = input("¿Nombre del modulo? ")
            if len(name.strip()) == 0:
                print(">>>ERROR. El nombre es invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def nomEst():
     while True:
        try:
            name = input("¿Nombre del estudiante? ")
            if len(name.strip()) == 0:
                print(">>>ERROR. El nombre es invalido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre.\n" + e)


def leerCodigo():
    while True:
        try:
            cod = input("Código del Estudiante ")
            if len(cod.strip()) == 0:
            # if cod < 0:
                print(">>> El Código es inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código.\n" + e)


def leerCodigoMod():
    while True:
        try:
            cod = input("Código del Modulo ")
            if len(cod.strip()) == 0:
            # if cod < 0:
                print(">>> El Código es inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código.\n" + e)


def leerCodigoGrup():

    while True:
        try:
            cod = input("Código del Grupo ")
            if len(cod.strip()) == 0:
            # if cod < 0:
                print(">>> El Código es inválido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el código.\n" + e)


def estudiantes_llegaron_tarde(lib, codMod, mes):
    arch = "Proyecto/acmeEducation.json"

    if codMod not in lib["Modulos"]:
        print(f"El código de módulo {codMod} no existe.")
        return []

    hora_inicio = datetime.strptime(lib["Modulos"][codMod]["Hora Inicio"], "%H:%M")
    tarde_estudiantes = []

    for fecha, asistencia in lib["Modulos"][codMod].get("Asistencia", {}).items():
        if fecha.split("/")[1] == mes:  # Verificar el mes
            for cod, datos in asistencia.items():
                if "Hora de Llegada" in datos:
                    hora_llegada = datetime.strptime(datos["Hora de Llegada"], "%H:%M")
                    if hora_llegada > hora_inicio + timedelta(minutes=15):
                        tarde_estudiantes.append(cod)

    # Almacenar el resultado en el JSON
    lib["Modulos"][codMod]["Informes"] = lib["Modulos"][codMod].get("Informes", {})
    lib["Modulos"][codMod]["Informes"]["EstudiantesTarde"] = tarde_estudiantes
    guardar(lib, arch)
    return tarde_estudiantes


def estudiantes_se_retiraron_antes(lib, codMod, mes):
    arch = "Proyecto/acmeEducation.json"
    if codMod not in lib["Modulos"]:
        print(f"El código de módulo {codMod} no existe.")
        return []

    hora_fin = datetime.strptime(lib["Modulos"][codMod]["Hora Fin"], "%H:%M")
    retirados_estudiantes = []

    for fecha, asistencia in lib["Modulos"][codMod].get("Asistencia", {}).items():
        if fecha.split("/")[1] == mes:  # Verificar el mes
            for cod, datos in asistencia.items():
                if ("Hora de Salida" not in datos or
                    (datetime.strptime(datos["Hora de Salida"], "%H:%M") < hora_fin - timedelta(minutes=10))):
                    retirados_estudiantes.append(cod)

    # Almacenar el resultado en el JSON
    lib["Modulos"][codMod]["Informes"] = lib["Modulos"][codMod].get("Informes", {})
    lib["Modulos"][codMod]["Informes"]["EstudiantesRetiradosAntes"] = retirados_estudiantes
    guardar(lib, arch)
    return retirados_estudiantes


def estudiantes_sin_faltas(lib, codMod, mes):
    arch = "Proyecto/acmeEducation.json"
    estudiantes_faltas = set()
    
    for fecha, asistencia in lib["Modulos"][codMod].get("Asistencia", {}).items():
        if fecha.split("/")[1] == mes:  # Verificar el mes
            for cod, datos in asistencia.items():
                hora_inicio = datetime.strptime(lib["Modulos"][codMod]["Hora Inicio"], "%H:%M")
                hora_fin = datetime.strptime(lib["Modulos"][codMod]["Hora Fin"], "%H:%M")
                
                # Verificar si llegó tarde
                if "Hora de Llegada" in datos:
                    hora_llegada = datetime.strptime(datos["Hora de Llegada"], "%H:%M")
                    if hora_llegada > hora_inicio + timedelta(minutes=15):
                        estudiantes_faltas.add(cod)

                # Verificar si se retiró temprano
                if ("Hora de Salida" not in datos or
                    (datetime.strptime(datos["Hora de Salida"], "%H:%M") < hora_fin - timedelta(minutes=10))):
                    estudiantes_faltas.add(cod)

    todos_estudiantes = set(lib["Estudiantes"].keys())
    sin_faltas = list(todos_estudiantes - estudiantes_faltas)
    
    # Almacenar el resultado en el JSON
    if "Informes" not in lib["Modulos"][codMod]:
        lib["Modulos"][codMod]["Informes"] = {}
    lib["Modulos"][codMod]["Informes"]["EstudiantesSinFaltas"] = sin_faltas
    guardar(lib,arch)
    
    return sin_faltas


def porcentaje_asistencia_por_modulo(lib, codMod, mes):
    arch = "Proyecto/acmeEducation.json"
    if codMod not in lib["Modulos"]:
        print(f"El código de módulo {codMod} no existe.")
        return 0

    total_estudiantes = lib["Modulos"][codMod].get("num_Integrantes", 0)
    estudiantes_asistieron = 0

    for fecha, asistencia in lib["Modulos"][codMod].get("Asistencia", {}).items():
        if fecha.split("/")[1] == mes:  # Verificar el mes
            for cod, datos in asistencia.items():
                hora_inicio = datetime.strptime(lib["Modulos"][codMod]["Hora Inicio"], "%H:%M")
                hora_fin = datetime.strptime(lib["Modulos"][codMod]["Hora Fin"], "%H:%M")
                hora_llegada = datetime.strptime(datos.get("Hora de Llegada", "00:00"), "%H:%M")
                hora_salida = datetime.strptime(datos.get("Hora de Salida", "00:00"), "%H:%M")

                # Verificar si llegó a tiempo y salió a tiempo
                if (hora_llegada <= hora_inicio + timedelta(minutes=15) and
                    hora_salida >= hora_fin - timedelta(minutes=10)):
                    estudiantes_asistieron += 1

    # Asegurarse de no dividir por cero
    if total_estudiantes == 0:
        return 0

    porcentaje = (estudiantes_asistieron / total_estudiantes) * 100

    # Almacenar el resultado en el JSON
    lib["Modulos"][codMod]["Informes"] = lib["Modulos"][codMod].get("Informes", {})
    lib["Modulos"][codMod]["Informes"]["PorcentajeAsistencia"] = porcentaje
    guardar(lib,arch)
    return porcentaje



def Inicio_sesion(lib, arch):
    print("\n" + "*" * 60)
    print("** ACME Education **\n".center(60))
    print("*" * 60)
    archivo = "Proyecto/acmeEducation.json"
    lib = cargar(archivo)
    
    Usuario = input((">>> INGRESE SU USUARIO <<<\nUSUARIO>>> "))
    if "Usuario" not in lib:
     print("")
     print(">>> BIENVENIDO ", Usuario, ". CONTINUAREMOS CON TU REGISTRO <<<")
     lib["Usuario"] = {}
     if Usuario not in lib["Usuario"]:
        contra = "SISGESA"
        print("\n>> Tu contraseña es >> ", contra)
        contras = encriptar_contraseña(contra)
        data ={
            "contrase": contras
        }
        lib["Usuario"][Usuario] = data
        sw = True
        while sw:
            try:
                password = input("\n>>> INGRESE SU CONTRASEÑA <<<\nCONTRASEÑA>>> ")
                verificacion = verificar_contraseña(password, contras)
                if verificacion:
                    print("\n*** Para continuar al Menú Ingrese su contraseña nuevamente ***")
                    sw = False
                else:
                    print(">>>ERROR. Contraseña Incorrecta\n")
            except Exception as e:
                print(">>> ERROR. ", e)
                
    qr = True
    while qr:
        try:
            if Usuario not in lib["Usuario"]:
                print (">>>ERROR. Usuario Incorrecto\n")
                Usuario = input((">>> INGRESE SU USUARIO <<<\nUSUARIO>>> "))
                continue
            qr = False
            contras = lib["Usuario"][Usuario]["contrase"]
            sw = True
            while sw:
                    try:
                        password = input("\n>>> INGRESE SU CONTRASEÑA <<<\nCONTRASEÑA>>> ")
                        verificacion = verificar_contraseña(password, contras)
                        if verificacion:
                            print("")
                            print(" ** BIENVENIDO ** ".center(50))
                            sw = False
                        else:
                         print(">>>ERROR. Contraseña Incorrecta\n")
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(">>> ERROR. ", e)



    
    guardar(lib, arch)


     


 

def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode('utf-8')).hexdigest()

def verificar_contraseña(contraseña_ingresada, hash_guardado):
    # Generar el hash de la contraseña ingresada
    hash_ingresado = encriptar_contraseña(contraseña_ingresada)
    # Comparar con el hash guardado
    return hash_ingresado == hash_guardado















































