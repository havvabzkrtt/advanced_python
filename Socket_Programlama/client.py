# server.py ve client.py iki ayrı terminalde çalıştırılır

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET : IPv4 formatını belirten sabit
# SOCK_STREAM : TCP protokolünü belirten sabit 

HOST = socket.gethostbyname(socket.gethostname())  # local host tanımlanabilir ama dinamik olmalı
PORT = 12345 # 0'dan 65535'e kadar rastgele bir sayı verilebilir

client_socket.connect((HOST, PORT))

message = client_socket.recv(1024) # client_socket üzerinden recv metodu ile ilgili hat dinlenerek serverdan gelen mesaj alınır  # 1024: maksimum veri boyutu 

print(message.decode("utf-8")) # decode ederek ekrana yazdırılır 

client_socket.close()
