import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())  # server socketi dinamik olarak oluşturulur 
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTESIZE = 1024 # bilgi kapasitesi
DISCONNECT_MESSAGE = "quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)  # Client, sunucuyla bir bağlantı kurar.s

# Döngü içerisinde client, serverdan mesaj alır ve cevap gönderebilir.
while True:
    message = client.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print("cikis yapiliyor...")
        break
    else:
        print(f"{message}\n")
        message = input("mesaj: ")
        client.send(message.encode(FORMAT))

client.close() 