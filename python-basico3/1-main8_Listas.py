

from http import client
from logging import getLogger
from operator import index
from os import remove
from re import search
from textwrap import indent
from turtle import circle, update


import sys

clients = ['pablo' , 'ricardo' , 'rocio']

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')


def list_client():
    for index, client in enumerate(clients):
        print('{}; {}'.format(index, client))


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('=' * 100)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[U]pdate')
    print('[S]earch client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_not_client():
    return input('Client is not in clients list')
    

def update_client(client_name, update_name):
    global clients

    if  client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_name
    else: 
        _get_not_client()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else: 
        _get_not_client()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else: 
            return True

    
if __name__ == '__main__':
    _print_welcome()
    'para poder ingresar datos desde consola'
    command = input()  
    command = command.upper()

    if command == 'C':
        list_client()
        client_name = _get_client_name()
        create_client(client_name)
        list_client()
    elif command == 'L':
        list_client()
    elif command == 'D':
        list_client()
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
    elif command == 'U':
        list_client()
        client_name = _get_client_name()
        update_name = input ('what is the updated client name?: ')
        
        update_client(client_name, update_name)
        list_client()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found: 
            print('The Client is in the clients list')
        else: 
            print('The client: {} is not our clients list' .format(client_name))
            
    else: 
        print('Invalid Command')
