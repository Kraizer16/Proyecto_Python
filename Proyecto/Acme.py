from Interfaz.Menu import Menu2, subMenu, subMenuAsis, subMenuInforAsis
from Modelo.modelo import  *
from Persistencia_Datos.Persistencia import cargar

acmeEducation = {}
archivo = "Proyecto/acmeEducation.json"
acmeEducation = cargar(archivo)

acmeEducation = Inicio_sesion(acmeEducation, archivo)


while True:
    op = Menu2()
    match op:
        case 1:
            acmeEducation = insertarGrup(acmeEducation, archivo)
        case 2:
             acmeEducation = insertarMod(acmeEducation, archivo)
        case 3:
             acmeEducation = insertarEst(acmeEducation, archivo)
        case 4:
            acmeEducation = insertDocAsigEst(acmeEducation, archivo)
        case 5:
            while True:
                opSub = subMenuAsis()
                match opSub:
                        case 1:
                            acmeEducation = registrarAsisLlegada(acmeEducation, archivo)
                        case 2:
                            acmeEducation = registrarAsisSalida(acmeEducation, archivo)
                        case 3:
                            print("\n\nGracias por usar el software.\n".center(40))
                            break
        case 6:
            while True:
                opSub = subMenu()
                match opSub:
                        case 1:
                            consultarGroup(acmeEducation)
                        case 2:
                            consultarMod(acmeEducation)
                        case 3:
                            consultarDoc(acmeEducation)
                        case 4:
                            consultarDocImpar(acmeEducation)
                        case 5:
                            print("\n\nGracias por usar el software.\n".center(40))
                            break
        case 7:
            while True:
                opSub = subMenuInforAsis()
                match opSub:
                        case 1:
                            consultarEstudiantesTarde(acmeEducation)
                        case 2:
                            consultarEstudiantesRetiradosAntes(acmeEducation)
                        case 3:
                            consultarEstudiantesSinFaltas(acmeEducation)
                        case 4:
                            consultarPorcentajeAsistencia(acmeEducation)
                        case 5:
                            print("\n\nGracias por usar el software.\n".center(40))
                            break
        case 8:
            acmeEducation = cambiarContra(acmeEducation, archivo)
        case 9:
            print("\n\nGracias por usar el software.\n".center(40))
            break

