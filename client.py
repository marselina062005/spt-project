import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Masukkan username: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Koneksi ke server terputus.")
            client.close()
            break

def write():
    while True:
        message = f"{username}: {input('')}"
        try:
            client.send(message.encode('utf-8'))
        except:
            print("Koneksi terputus, pesan tidak terkirim.")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()