import socket 


s=socket.socket()
host = input("Please Enter hostname: ")
port=1234
try:
    s.connect((host,port))
    print("Connected to server")
except:
    print("Not  able to connect tio server")
while 1:
    incoming_msg=s.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Server: ",incoming_msg)
    message=input("You: ")
    message=message.encode()
    s.send(message)
