import sys
import socket
import selectors
import types
import os
import sqlite3

sel = selectors.DefaultSelector()

HOST = "127.0.0.1"
PORT = 65432


os.system("cls")
print("Servidor iniciado")
i = 1


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Conectando: {addr}")
            while True:
                data = conn.recv(1024)


                if not data:
                    break
                a = str(data).split("-")
                if len(a) == 2 and a[0] == "b'2":
                    print("Eliminando ID: "+str(a[1]))
                    connn = None
                    try:
                        connn = sqlite3.connect(r"C:\Users\Samael\Desktop\ServerClient\universidad.db")
                        sql = ''' DELETE FROM Alumnos WHERE ID = ?'''
                        cur = connn.cursor()
                        project = (a[1].replace("'",""))
                        
                        cur.execute(sql, project)
                        connn.commit()
                        datatext = "Eliminado con exito"
                        #connn.commit()
                        conn.sendall(str.encode(datatext))
                    except Error as e:
                        print(e)
                    
                    
                elif str(data) == "b'4'":
                    connn = None
                    try:
                        connn = sqlite3.connect(r"C:\Users\Samael\Desktop\ServerClient\universidad.db")
                        sql = ''' SELECT * FROM Alumnos'''
                        cur = connn.cursor()
                        cur.execute(sql)
                        rows = cur.fetchall()
                        datatext = ""
                        for row in rows:
                            datatext += str(row).replace("(","").replace(")","")+"||"
                            print(str(row))
                        #connn.commit()
                        conn.sendall(str.encode(datatext))
                    except Error as e:
                        print(e)
                            
                else:
                    print("data: "+str(data))
                    temp = str.split(str(data),"|")
                    
                    data1 = temp[0].replace("b'","")
                    data2 = temp[1]
                    data3 = temp[2].replace("'","")
                    
                    project = (data1,data2,data3)
                    
                    connn = None
                    try:
                        connn = sqlite3.connect(r"C:\Users\Samael\Desktop\ServerClient\universidad.db")
                        print("Se hizo la conexión a la DB éxitosamente")
                        sql = ''' INSERT INTO Alumnos(ALUMNO,MATRICULA,CARRERA) VALUES(?,?,?) '''
                        cur = connn.cursor()
                        cur.execute(sql, project)
                        connn.commit()
                    except Error as e:
                        print(e)
                    
                   
                    conn.sendall(data)
                
