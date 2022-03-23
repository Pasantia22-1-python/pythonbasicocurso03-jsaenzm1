

from dataclasses import field
from http import client
from logging import getLogger
from operator import index
from os import remove
from re import search
from textwrap import indent
from turtle import circle, position, update


import sys

'Diccionario'
clients = [
    {
        'name': 'pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_client():
    for index, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid= index, 
            name= client['name'],
            company= client['company'], 
            email= client['email'], 
            position= position['position']))


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('=' * 100)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[U]pdate')
    print('[S]earch client')


def update_client(idclient, update_name):
    global clients

    if len(clients) - 1 >= idclient:
        clients[idclient] = update_client
    else: 
        _get_not_client()


def delete_client(idclient):
    global clients

    for index, client in enumerate(clients):
        if index == idclient:
            del clients[index]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else: 
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the clients {}: '.format(field_name))
    return field


def _get_client():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }
    return client


def _get_not_client():
    return input('Client is not in clients list')
    
    
if __name__ == '__main__':
    _print_welcome()
    'para poder ingresar datos desde consola'
    command = input()  
    command = command.upper()

    if command == 'C':
        client = _get_client()
        create_client(client)
        list_client()
    elif command == 'L':
        list_client()
    elif command == 'D':
        list_client()
        idclient = int(_get_client_field('id'))
        delete_client(idclient)
        list_client()
    elif command == 'U':
        list_client()
        idclient = int(_get_client_field('id'))
        update_name = _get_client()
        update_client(idclient, update_name)
        list_client()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found: 
            print('The Client is in the clients list')
        else: 
            print('The client: {} is not our clients list' .format(client_name))
            
    else: 
        print('Invalid Command')
