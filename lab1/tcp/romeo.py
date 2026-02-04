import socket

to_send = ['line0']
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.10.0.101',4000)) # IP of Juliet

for line in to_send: 
    sock.send(line.encode('utf-8')+b'\n')

sock.shutdown(socket.SHUT_WR)

while True:
    data = sock.recv(4096)
    if not data:
        break
    lines = data.decode('utf-8').strip().split('\n')
    for line in lines:
        print(line)