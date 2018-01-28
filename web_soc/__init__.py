import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('Socket Created')

# To allow you to immediately reuse the same port after
# killing your server:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = 'localhost'
port = 8000

s.connect((host, port))

print('Socket Connected to ' + host + ' on port ', port)

# Send some data to server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Send the whole string(sendall() handles the looping for you)
    s.sendall(message.encode('utf8'))
except socket.error:
    print('Send failed')
    sys.exit()

print('Message sent successfully')

# Now receive data
data = []

while True:
    chunk = s.recv(4096)  # blocks while waiting for data
    if chunk:
        data.append(chunk.decode("utf8"))
    # If the recv() returns a blank string, then the other side
    # closed the socket, and no more data will be sent:
    else:
        break

print("".join(data))
