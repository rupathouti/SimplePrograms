import socket;

conn = socket.socket()

conn.connect(("localhost",8091))

while True:
  data = raw_input("Enter a Message> ")
  conn.send(data.encode(encoding='utf_8',errors='strict'))
