import socket
s=socket.socket()
host = socket.gethostname()
print(host)
print("Server will start on host:", host)
port=1234
s.bind((host, port))
print("server bound succesfully!!")
s.listen(1)
conn, addr= s.accept()
print(addr, "Has been connected!")
while True:
    message=input("Server:  ")
    message=message.encode()
    conn.send(message)
    incoming_msg=conn.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Client:  ", incoming_msg  )
    
    
   


    
