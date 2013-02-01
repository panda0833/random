net = require("net")
HOST = '127.0.0.1'
PORT = 6969

net.createServer(  (sock) =>
	#console.log("Conn: " +  sock.remoteAddress)
	sock.on 'data', (data)  =>
		#console.log('Data' + data) 
		sock.write('world')
	
	sock.on 'close', =>
		#console.log('closed')

	).listen(PORT, HOST)

console.log "Listening on " + HOST + " " + PORT




