def Menu2():
    while True:
        
        print("")
        print(">>> MENU <<<".center(50))
        print("*" * 60)
        print("1. Registro de Grupos")
        print("2. Registro de Módulos")
        print("3. Registro de Estudiantes")
        print("4. Registro de Docentes")
        print("5. Registro de Asistencia")
        print("6. Consultas de Información")
        print("7. Generar Informes")
        print("8. Cambiar Contraseña")
        print("9. Salir")
        print("*" * 60)

        print("Opcion? >>> ", end="")
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 9:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
            return opcion
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")

def subMenu():
    while True:
        print("\n" + "*" * 60)
        print("** 6. Consultas de información **".center(60))
        print("*" * 60)
        print("1. Estudiantes Matriculados en un Grupo")
        print("2. Estudiantes Inscritos en un Modulo")
        print("3. Docentes que imparten un Modulo")
        print("4. Estudiantes que están bajo la responsabilidad\n   de un docente en un determinado módulo.")
        print("5. Volver")
        print("*" * 60)

        print("Opcion? >>> ", end="")  

        try:
            opcionSub = int(input())
            if opcionSub < 1 or opcionSub > 5:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
                continue
            return opcionSub
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")

def subMenuAsis():
    while True:
        print("\n" + "*" * 60)
        print("** 5. Registrar Asistencia **\n".center(50))
        print("*" * 60)
        print("1. Registre Su hora de Llegada")
        print("2. Registres Su hora de Salida")
        print("3. Volver")
        print("*" * 60)

        print("Opcion? >>> ", end="")
        try:
            opcionSub = int(input())
            if opcionSub < 1 or opcionSub > 3:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
                continue
            return opcionSub
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")

def subMenuInforAsis():
    while True:
        print("\n" + "*" * 60)
        print("** 6. Informes de Asistencia **\n".center(50))
        print("*" * 60)
        print("1. Estudiantes que han llegado tarde a un módulo en un mes específico\n")
        print("2. Estudiantes que se retiraron antes de la finalización de una sesión en un mes específico. \n")
        print("3. Estudiantes que no han faltado a ningún módulo durante un mes. \n")
        print("4. Porcentaje de asistencia por módulo \n")
        print("5. Volver")
        print("*" * 60)

        print("Opcion? >>> ", end="")
        try:
            opcionSub = int(input())
            if opcionSub < 1 or opcionSub > 5:
                print("ERROR. Opción NO válida")
                input("Presione cualquier tecla para volver al menu...")
                continue
            return opcionSub
            
        except ValueError:
            print("ERROR. Opción NO válida")
            input("Presione cualquier tecla para volver al menu...")


