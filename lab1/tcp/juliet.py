import socket

to_send = ['line1', 'line2']
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.10.0.101',4000)) # IP of Juliet
sock.listen()
conn_sock, conn_addr = sock.accept()

while True: 
    data = conn_sock.recv(4096)
    if not data:
        break
    lines = data.decode('utf-8').strip().split('\n')
    for line in lines:
        print(line)


for line in to_send: 
    conn_sock.send(line.encode('utf-8')+b'\n')

conn_sock.shutdown(socket.SHUT_RDWR)