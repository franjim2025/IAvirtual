def suma (a, b):
    resultado = a + b
    return(resultado)
def resta (a, b):
    resultado = a - b
    return(resultado)
def multiplicar (a, b):
    resultado = a * b
    return(resultado)
def dividir (a, b):
    resultado = a / b
    return(resultado)
n= int(input("ingrese el primer número: "))
m= int(input("ingrese el segundo número: "))
bandera = True
while bandera:
    print("Cual operación deseas realizar: ")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("el resultado es: ",suma(n,m))
       
    elif opcion == 2:
        print("el resultado es: ",resta(n,m))
   
    elif opcion == 3:
        print("el resultado es: ",multiplicar(n,m))
    elif opcion == 4:
        print("el resultado es: ",dividir(n,m))
    elif opcion == 5:
        bandera= False
    else:
        print("Opción no válida")
print("Fin del programa")
