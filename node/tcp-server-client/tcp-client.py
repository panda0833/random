import socket, datetime

num_of_requests = 20000
print "sending " + str(num_of_requests)+ " requests" 


then = datetime.datetime.now()

for x in range(num_of_requests):
	soc = socket.create_connection( ("127.0.0.1", 6969))
	soc.sendall("Hello")
	soc.recv(5)
	soc.close()	

now = datetime.datetime.now() 

print "it took: " + str(now-then)
