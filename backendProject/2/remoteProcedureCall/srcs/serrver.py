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
        return params[::-1]
    
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
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

        print('starting up on {}'.format(self.server_address))
        self.sock.bind(self.server_address)
        self.sock.listen(1)
    
    def listen(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print('connection from'+str(client_address))

        
        