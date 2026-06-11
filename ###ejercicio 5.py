###ejercicio 5
nombre = input("ingrese su nombre: ")
nota= float(input("infrese su nota final: "))
if nota < 4.0:
    print("REPROBADO")
if nota >= 4.0:
    asistencia=input("¿tuvo mas de 80%  de asistencia?")
    asistencia=asistencia.lower()
    if asistencia =="si":
        print("Asignatura aprobada")
    else:
        print("no aprueba por asistencia")