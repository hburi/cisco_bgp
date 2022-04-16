#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Abril 2022
Autor: Héctor Fernando Buri

Funciones para cisco_bgp.py - CISCO
"""

'''
Pigué
ssh -l admin -p 6622 190.103.207.225	
admin	w3tcb4!
'''


#https://es.ephesossoftware.com/articles/programming/how-to-read-and-write-to-google-sheets-with-python.html
# Ejemplos para escribir en google sheets

import paramiko
import re

enter = '\n'

ip = '190.103.207.225'
port = 6622
user = "admin"
password = "w3tcb4!"

command = 'show ip bgp neigh ' + enter
#print (command)


def conn_command(hostname,username, password, port, order):
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
    
    stdin, stdout, stderr = ssh.exec_command(order)
    output = stdout.readlines()
    ssh.close()
    return(output)
    


def ip_finder(text):
    
    'Devuelve una lista con las IP que encuentre en el texto de entrada'
    
    ip = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
    #is_ip = bool(ip.findall(text))
    return ip.findall(text)

def net_finder(text):
    
    'Devuelve una lista con las redes que encuentre en el texto de entrada'
    
    ip = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+')
    #is_ip = bool(ip.findall(text))
    return ip.findall(text)


def only_number_finder(text):
    
    'Devuelve los numeros aislados en un texto de entrada'
    
    number = re.compile('\s[0-9]+\,')

    return number.findall(text)
    

def name_finder(text):
    
    'Remueve la cadena "Description: " de una cadena'
    
    ip = re.compile('[^Description:  ]+[^\r\n]')
    
    list_name = ip.findall(text)
    
    
    return ''.join(list_name)


