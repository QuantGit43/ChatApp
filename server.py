import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(1)
conn_socket, addres  = sock.accept()

while True:
    data = conn_socket.recv(1024)
    if not data:
        break
    conn_socket.send(data.upper())

conn_socket.close()