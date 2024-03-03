import os
import json

config=json.load(open('config.json'))

if os.path.exists(config['filepath']):
    os.remove(config['filepath'])

os.mkfifo(config['filepath'],0o600)

print("FIFO named '%s' created successfully" % config['filepath'])
print("Type in what you want to send to client")

flag=True

while flag:
    inputstr=input()

    if inputstr=='exit':
        flag=False
    else:
        with open(config['filepath'], 'w') as f:
            f.write(inputstr)

os.remove(config['filepath'])