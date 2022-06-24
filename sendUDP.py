from machine import Pin, ADC, I2C
import socket
import utime

sensor = ADC(Pin(36))
p1 = Pin(16)
p2 = Pin(14)
volts = sensor.read()
#las config de la red el port siempre debe ser el mismo en ambos codes
UDP_IP = '172.16.4.95'
UDP_PORT = 8889
sv = str(volts)
UDP_PAYLOAD = sv
#Muevele a la red que estes usando
SSID = "Students"
PASSWORD = "P0l1t3cn1c4.b1s"

# FUNCIÓN PARA ESTABLECER LA CONEXIÓN WIFI (STATION)
def do_connect(SSID, PASSWORD):
    import network                            # importa el módulo network
    global sta_if
    sta_if = network.WLAN(network.STA_IF)     # instancia el objeto -sta_if- para realizar la conexión en modo STA 
    if not sta_if.isconnected():              # si no existe conexión...
        sta_if.active(True)                   # activa el interfaz STA del ESP32
        sta_if.connect(SSID, PASSWORD)        # inicia la conexión con el AP
        print('Dame un momento, wey. Me estoy conectando a ', SSID +"...")
        while not sta_if.isconnected():           # ...si no se ha establecido la conexión...
            pass                                  # ...repite el bucle...
    print('Configuración de red (IP/netmask/gw/DNS):', sta_if.ifconfig())
do_connect(SSID,PASSWORD)

#este es un plus de envio por consolo, hay que pasarlo a botones
def yes_or_no(question):
    reply = str(input(question)).lower().strip()
    if reply[0] == 'y':
        return 0
    elif reply[0] == 'n':
        return 1
    else:
        return yes_or_no("Please Enter (y/n) ")
   
while True:
    volts = sensor.read() #Read Audio

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create the socket of connection
    sock.sendto(bytes(UDP_PAYLOAD, "utf-8"), (UDP_IP, UDP_PORT))  #Config of the UDP and send method
    sock.close() #Close the connection


