import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())  # server socketi dinamik olarak oluşturulur 
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8" 
BYTESIZE = 1024  # bilgi kapasitesi
DISCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()  # Server bir soket oluşturur ve belirtilen adreste bağlantıları dinler.
print("server calisiyor...\n")

client_socket, client_address = server.accept() # bağlantı adresi ve socketi alınır
client_socket.send("server baglantiniz yapildi.\n".encode(FORMAT)) 
# Server, gelen bağlantıyı kabul eder ve cliente bir mesaj gönderir.

# Server, döngü içinde clientten mesajlar alır ve cevap verir.
while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print("cikis yapildi...")
        break
    else:
        print(f"{message}\n")
        message = input("mesaj: ")
        client_socket.send(message.encode(FORMAT))

server.close()
client_socket.close() 




