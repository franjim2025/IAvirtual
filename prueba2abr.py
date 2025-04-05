from datetime import date

def calcular_edad():
    # Solicitar la fecha de nacimiento
    dia = int(input("Ingrese el día de nacimiento (DD): "))
    mes = int(input("Ingrese el mes de nacimiento (MM): "))
    anio = int(input("Ingrese el año de nacimiento (AAAA): "))

    fecha_actual = date.today()    
    
    fecha_de_nacimiento = date(anio, mes, dia)
    edad = fecha_actual.year - fecha_de_nacimiento.year

    print(edad)

calcular_edad()
