import socket
import os



os.system("cls")

HOST = "127.0.0.1"  # IP DEL SERVIDOR
PORT = 65432  # Puerto usado en el servidor
os.system("cls") # Limpia contenido de la consola para darle un acceso más limpio (cliente)

menu_options = { # este es el menú de opciones con el cual damos las opciones al cliente
    1: 'Añade un alumno',
    2: 'Elimina un alumno',
    3: 'Modifica un alumno',
    4: "Muestrame todos los alumnos",
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys(): #va desde el 1 al 5
        print (key, '--', menu_options[key] ) #imprimimos las opciones desde el 1 al 5

def option1():
     print("By DaaNN")
     a = input("Nombre:\n")
     b = input("Matricula:\n")
     c = input("Carrera:\n")
     print("Enviado datos al servidor")
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((HOST, PORT))
         dataset = str(a)+"|"+str(b)+"|"+str(c)
         s.sendall(str.encode(dataset))
         data = s.recv(1024)
         print(f"Recibe {data!r}")

def option2():
     print("By DaaNN")
     a = input("ID a eliminar:\n")
     print("Enviado datos al servidor")
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((HOST, PORT))
         dataset = "2-"+a
         s.sendall(str.encode(dataset))#+str(a)+"|"+str(b)+"|"+str(c)
         data = s.recv(1024)
         print(f"Recibe {data!r}")
     

def option3():
     print('Se hizo la opción 3\'')

def option4():
     print('Se hizo la opción 4\'')
     print("Enviado datos al servidor")
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         s.connect((HOST, PORT))
         dataset = "4"
         s.sendall(str.encode(dataset))#+str(a)+"|"+str(b)+"|"+str(c)
         data = s.recv(1024)
         rows = str(data).replace('b\"',"").replace('\"',"").split("||")
         for colum in rows:
            print(colum)

while(True):
    print_menu()
    option = ''
    try:
        option = int(input('Bienvenido, ¡ingresa una opción!: '))
    except:
        print('¿Quizá tecleaste algo que no fue un número?, verificalo')
    if option == 1:
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        print('¿Adiós?')
        exit()
    else:
        print('¿Número inválido?, por favor teclea del 1 al 5')
