import socket #importamos librerias
import serial
import time

arduino = serial.Serial('/dev/ttyUSB0',9600, timeout = 1) #objeto serial llamado "arduino"
arduino.flushInput() #Limpiamos el input buffer serial 
arduino.flushOutput() #Limpiamos el output buffer serial

print 'Starting Serial! \n ' # Escribimos 

TCP_IP = '192.168.1.7' #IP de nuestro servidor
TCP_PORT = 5005 # puerto TCP 
BUFFER_SIZE = 20 # Tamaño del buffer 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Abrir socket
s.bind((TCP_IP, TCP_PORT)) #Levantar el servidor
s.listen(1) #Esperar 1 conexion. Accion bloqueadora

print 'Esperando conexion...\n\n' # Escribir

conn, addr = s.accept() #Aceptar la conexion solicitada

print 'Conectado con: ', addr 

while 1:
	data = conn.recv(BUFFER_SIZE) #Recibir datos a traves del socket
	if len(data) > 0: #Si hay data recibida en el Buffer del TCP
		arduino.write(data) #Escribimos los datos en el puerto serial arduino
		print "Enviado Arduino: ", data #Se imprime en pntalla lo que se envio al arduino 
		if data == 't': #Si el mensaje recibido TCP y enviado Serial es "t"
			tempRead = arduino.readline()#leemos el puerto arduino y lo guardamos en "tempRead"
			print tempRead #imprimimos en pantalla los datos adquiridos de la conexion serial con el arduino
			conn.send(tempRead) # Envio a traves de TCP de los datos obtenidos en arduino 
		if data == 'r': #Si el mensaje recibido es r 
			revRead = arduino.readline()#leemos serial
			print revRead#imprimimos en pantalla
			conn.send(revRead)#enviamos por TCP

arduino.close()#Cerramos el puerto serial
conn.close()#Cerramos el puerto TCP

