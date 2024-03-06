# このステージでは、クライアントがサーバに接続する形式のチャットメッセンジャーサービスを作成します。サーバはバックグラウンドで稼働し、一方でクライアントは CLI を通じてサーバに接続します。接続が確立された後、クライアントはメッセージを入力してサーバに送り、そのメッセージはサーバに接続している他の全てのクライアントにも配信されます。

import socket 
import threading
import sys
import os

class Client:
    def __init__(self)->None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = 'localhost'
        self.server_port = 10000
        self.client_port = 10001
        self.buffer_size = 4096
    
    def set_sock_bind(self):
        self.sock.bind((self.server_address, self.client_port))

    def unlink_sock(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

    def prepare_receive(self):
        self.unlink_sock()
        self.set_sock_bind()

    
    def receive_message(self):
        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            if data:
                decoded_data = data.decode()
                print(f"Received message from {addr}: {decoded_data}")
                return decoded_data, addr
            else:
                print("No message received")
                break
    
    def make_message(self, message:str):
        return message.encode()
    
    def send_message(self, message:bytes, addr):
        self.sock.sendto(message, addr)
        print(f"Sent message to {addr}: {message.decode()}")
    
    def close_sock(self):
        print("Closing socket")
        self.sock.close()
    
    def run(self):
        self.set_sock_bind()
        try:
            while True:
                message=self.make_message(input("Enter message: "))
                self.send_message(message, (self.server_address, self.server_port))
                print("Waiting to receive message")
                self.receive_message()
                if message.decode() == "exit":
                    break
        finally:
            self.close_sock()
    
def main():
    client = Client()
    client.run()

if __name__ == "__main__":
    main()
