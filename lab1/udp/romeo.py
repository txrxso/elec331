import socket

send_to_juliet = ['line0']

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM for UDP
sock.bind(('10.10.0.100', 4000)) # Bind to Romeo's IP and port 4000 to reserve

for line in send_to_juliet:
    sent = sock.sendto(line.encode('utf-8'), ('10.10.0.101', 5000)) # Juliet's IP and port 5000
    print("Sent message:", line)

for i in range(4):
    data, addr = sock.recvfrom(1024) # Buffer size is 1024 bytes
    line = data.decode('utf-8')
    print("Received message:", line)

sock.close()