from modulos2 import * 
nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]
apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
f=True
while (f==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("Que te gustaría hacer?")
    print("1.Agregar estudiante")
    print("2. Ver estudiantes")
    print("3.Eliminar estudiante")
    print("4.cambiar nombre o apellido")
    print("5.Salir del programa")
    opcionUsuario= int(input(":"))
    if(opcionUsuario==2):
        print("Lista estudiantes:")
        lista(nombres,apellidos)
    elif(opcionUsuario==5):
        f= False
        break
    elif(opcionUsuario==1):
        nombreEstudiante=input("Que nombre te gustaría agregarle al estudiante:")
        
        apellidoestudiante=input("Que apellido te gustaria poner al estudiante")
        
        ag(nombres,nombreEstudiante,apellidos,apellidoestudiante)
        
        print("Lista nueva de estudiantes:")
        
    elif(opcionUsuario==3):
        ##Indicar cuántas veces debe recorrerlo de acuerdo al tamaño de la lista
        lista(nombres,apellidos)
        c=int(input("Cual estudiante quieres eliminar?:"))
        hola(nombres,apellidos,c,nombres,apellidos)

       
        

    elif(opcionUsuario==4):
        n=int(input("ingrese el numero del estudiante que quiera editar: "))
        n=n-1
        NombreEditado=input("ingrese el numevo nombre para el estudiante: ")
        ApellidoEditado=input("ingrese el apellido que quiera editar")
        editar(nombres,n,NombreEditado,apellidos,ApellidoEditado)
        y=int(input("¿quiere seguir editando? (1=si)//(2=no)"))

        lista(nombres,apellidos)