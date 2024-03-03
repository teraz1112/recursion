import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = './udp_socket_file'

address='./udp_client_socket_file'

message = b'This is the message. Test 1 2 3 4 5 6 7 8 9 10'

sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()