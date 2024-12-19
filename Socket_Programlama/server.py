# server.py ve client.py iki ayrı terminalde çalıştırılır

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET : IPv4 formatını belirten sabit
# SOCK_STREAM : TCP protokolünü belirten sabit 

# HOST = "127.0.0.1"
HOST = socket.gethostbyname(socket.gethostname())  # local host tanımlanabilir ama dinamik olmalı
PORT = 12345 # 0'dan 65535'e kadar rastgele bir sayı verilebilir
# print(HOST) # 192.168.1.4 / kullanılan IP adresi getirilir. 

server_socket.bind((HOST, PORT)) # sockete bir adres belirtilir
 
server_socket.listen()  # dinleme işlemi 

while True:
    client_socket, client_address = server_socket.accept() # server a bağlanan clientlar ve adresleri alınır

    # client_address: clientın hangi port altında çalıştığını belirtir
    print(f"baglanti yapildi: {client_address}")  # client adresine mesaj gönderilir 
    print(client_socket, client_address)  

    client_socket.send("merhaba".encode("utf-8"))
    
    server_socket.close()
    break  # Tek Seferlik Bağlantı: Sunucu, ilk bağlantıyı kabul ettikten sonra kapanır (break kullanılmış).
 