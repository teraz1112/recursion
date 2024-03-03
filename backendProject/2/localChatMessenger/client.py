import socket
import sys
# ユーザーからの入力をサーバーに送信する。入力はコマンドラインから受け取る。

sock=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'

print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print('error:{}'.format(err))
    sys.exit(1)

try:
    message = input('input message:')
    sock.sendall(message.encode())

    sock.settimeout(5)

    try:
        while True:
            data = sock.recv(32)
            if data:
                print('received '+data.decode('utf-8'))
            else:
                break
    except(TimeoutError):
        print('timeout error')
finally:
    print('closing socket')
    sock.close()