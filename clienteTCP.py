import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 4826

BUFFER_SIZE = 20
msg = 'Hola Mundo!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
cnt = 1
while True:
    msg = raw_input('Ingrese el mensaje: ')
    s.send(msg) #Enviar el mensaje
    #print str(cnt)
    cnt += 1
    time.sleep(1) #Una vez cada segundo
s.close()
