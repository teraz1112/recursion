import json
import socket
import os
import math
import sys
import threading

class Process:
    @classmethod
    def process_method(cls, method,params):
        if method == 'floor':
            return Process.floor(params)
        elif method == 'nroot':
            return Process.nroot(params)
        elif method == 'reverse':
            return Process.reverse(params)
        elif method == 'validAnagram':
            return Process.validAnagram(params)
        elif method == 'sort':
            return Process.sort(params)
        else:
            return 'Invalid method'
    
    @staticmethod
    def floor(params):
        return math.floor(params[0])
    
    @staticmethod
    def nroot(params):
        n=params[0]
        x=params[1]
        return x**(1/n)
    
    @staticmethod
    def reverse(params):
        return params[0][::-1]
    
    @staticmethod
    def validAnagram(params):
        if len(params[0])!=len(params[1]) or len(params[0])==0 or len(params[1])==0:
            return False
        else:
            return sorted(params[0])==sorted(params[1])

    @staticmethod
    def sort(params):
        return sorted(params)

class Server:
    def __init__(self, server_address):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    def connect(self):
        sock=self.sock

        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        print('starting up on {}'.format(self.server_address))
        sock.bind(self.server_address)
        sock.listen(1)
    
    def listen(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print('connection from'+str(client_address))

                self.handle(connection, client_address)
            finally:
                connection.close()
    
    def handle(self, connection, client_address):
        while True:
            data = connection.recv(4096).decode('utf-8')
            if data:
                data_dict = json.load(data)
                print('received {!r}'.format(data_dict))

                method = data_dict['method']
                params = data_dict['params']
                id = data_dict['id']

                result = Process.process_method(method, params)
                result_dict = {}
                result_dict['result'] = result
                result_dict['result_type'] = type(result).__name__
                result_dict['id'] = id

                result_json = json.dumps(result_dict)
                connection.sendall(result_json.encode('utf-8'))
                print('sent {!r}'.format(result_dict))

            else:
                print('no data from', client_address)
                break
    
    def start(self):
        self.connect()
        self.listen()
                
if __name__ == '__main__':
    server = Server('socket_file')
    server.start()
        