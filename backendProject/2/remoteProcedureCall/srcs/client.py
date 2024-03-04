import json
import socket
import sys

class Client:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self):
        server_address=self.server_address
        print('connecting to {}'.format(server_address))
    
        try:
            self.sock.connect(server_address)
        except socket.error as msg:
            print(msg)
            sys.exit(1)

    def send(self):
        while True:
            try:
                print('sending message')
                with open('../json/sample2.json', 'r') as message:
                    if message:
                        message_dict = json.load(message)
                        self.sock.sendall(json.dumps(message_dict).encode('utf-8'))
                    else:
                        print('no message')
                        break

                response = self.sock.recv(4096).decode('utf-8')
                if response:
                    print(response)
                else:
                    print('no data from', self.server_address)
                    break
            except FileNotFoundError:
                print("The file was not found")
                break
            except json.JSONDecodeError:
                print("Could not decode the JSON file")
                break
            except socket.error as e:
                print("Socket error:", e)
                break
            finally:
                print('closing socket')
                self.sock.close()
                sys.exit()
                break
            
    def start(self):
        self.connect()
        self.send()

if __name__ == '__main__':
    client = Client('socket_file')
    client.start()