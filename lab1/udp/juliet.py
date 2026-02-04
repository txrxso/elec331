import socket

send_to_romeo = ['line1', 'line2']

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM for UDP
sock.bind(('10.10.0.101',5000)) # Bind to Juliet's IP and port 5000 to reserve

for i in range(7):
    data, addr = sock.recvfrom(1024) # Buffer size is 1024 bytes
    print("Received message:", data.decode('utf-8'))

# send back
for line in send_to_romeo:
    sock.sendto(line.encode('utf-8'), ('10.10.0.100', 4000)) # Romeo's IP and port 
    print("Sent message:", line)

sock.close()