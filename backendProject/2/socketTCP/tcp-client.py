import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = b'Sending a message to server from client using socket file connection. This is a test message.'
    sock.sendall(message)

    sock.settimeout(2)

    try:
        while True:
            data=str(sock.recv(32))

            if data:
                print('received '+data)
            else:
                break
    except(TimeoutError):
        print('timeout')

finally:
    print('closing socket')
    sock.close()