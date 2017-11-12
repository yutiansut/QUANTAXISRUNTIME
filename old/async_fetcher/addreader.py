import asyncio

import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s1.bind(('127.0.0.1',5125) )
s1.listen(10000)
connection, address = s1.accept()

loop = asyncio.get_event_loop()

def reader():
    data = connection.recv(100)
    print("Received:", data.decode())

    # We are done: unregister the file descriptor
    #loop.remove_reader(rsock)
    # Stop the event loop
    #loop.stop()
   

# Register the file descriptor for read event
loop.add_reader(connection, reader)

# Simulate the reception of data from the network



# Run the event loop
loop.run_forever()


#loop.call_soon(wsock.send, 'aqwq'.encode())

#loop.call_soon(wsock.send, 'aqwq'.encode())                                     
#loop.call_soon(wsock.send, 'aw'.encode())
# We are done, close sockets and the event loop


loop.close()