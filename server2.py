import socket;

print("Starting the Socket")
ss = socket.socket()

ss.bind(("localhost",8091))

ss.listen(5)

print("Waiting for client")
socket,add = ss.accept()
print("Connected to ",add)

while True:
  data = socket.recv(1067);
  print("Client sent -> ",data.decode())

ss.close()	
