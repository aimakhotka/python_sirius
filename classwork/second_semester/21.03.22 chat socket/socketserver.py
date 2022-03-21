import socket
from pprint import pprint
import threading

HOST = '127.0.0.1'
PORT = 12345

def enc(s):
    return s.encode('utf-8')

def dec(s):
    return s.decode('utf-8')


def new_client(client_socket):
    global users
    while True:
        recv_msg = client_socket.recv(1024)
        print('\nIncoming msg: \n')
        decoded = dec(recv_msg)
        print('User {0}: {1}:'.format(username, decoded))
        if decoded == 'q':
            del users[username]
            print('User {0} disconnected'.format(username))
            pprint(users)
            break
        
def server_auth(user):
    while True:
        user.send(enc('Type your name: '))
        username = dec(user.recv(1024))
        if username not in users.keys():
            print('User {0[0]}:{0[1]} connected as {1}'\
                .format(address, username))
            print('\nNow connected: \n')
            pprint(users)
            user.send(enc('Auth ok'))
            return username

if __name__ == '__main__':
    server_socket = socket.socket()

    server_socket.bind((HOST, PORT))
    server_socket.listen()
    users = dict() #addrs
    try:
        while True:
            user, address = server_socket.accept()
            print('\nConnected: ', address)
            username = server_auth(user)
            users[username] = address
            threading.Thread(target = new_client, \
                args = (user, username)).start()
        
    except KeyboardInterrupt:
        print('n\Server shut down!')
        server_socket.close()
    except Exception as e:
        print(e)
        server_socket.close()
    server_socket.close()