#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Abril 2022
Autor: Héctor Fernando Buri

Pruebas para leer y escribir una hoja de datos de google
"""


# sheet => '1B2yGYVR56Tx7gQ79b7543RvJPTgtmUJ_uTlsH3QqS3I'
# https://www.youtube.com/watch?v=n0EkLvSOWc8
# https://stackoverflow.com/questions/46287267/how-can-i-get-the-file-service-account-json-for-google-translate-api
# https://docs.gspread.org/en/latest/user-guide.html

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
#import pygsheets


# Scopes y autenticaciones (NO MODIFICAR)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
         



creds = ServiceAccountCredentials.from_json_keyfile_name('test1-347018-cfcd19c58eee.json', scope)
client = gspread.authorize(creds)

# Se enlaza a la hoja por nombre, el nombre puede variar

sheet = client.open("Ruteos_NODOCOOP").sheet1


enter = '\n'


diccionario = {('FASTNET', '10.5.0.13', 265768): [], ('SILICA BACKUP WILD', '10.32.1.13', 7049): ['168.227.206.0/24', '168.227.207.0/24', '170.79.16.0/22', '190.103.207.0/24'], ('SILICA CDN BACKUP WILD', '10.32.1.45', 7049): ['168.227.206.0/24', '168.227.207.0/24', '170.79.16.0/22', '181.189.164.0/24']}
lista = diccionario.keys()


def write_rows(dictionary):
    
    sheet.clear()
    
    key_peers = list(dictionary.keys())
    key_peers = [value for value in key_peers if dictionary[value] != []]

    time_stamp()
    names_row(dictionary)


    all_nets = []

    for peer in key_peers:
        nets = dictionary[peer]
        for net in nets:
            if net not in all_nets:
                all_nets.append(net)
                
                
    all_nets.sort()

    for network in all_nets:
        row_list = []
        row_list.append(network)
        for peers in key_peers:
            
            if network in dictionary[peers]:
                row_list.append('SÍ')
            else:
                row_list.append('NO')
        
        sheet.append_row(row_list, table_range='C3')


def fill_peer_names(diccionario):
    # Escribo los proveedores en la FILA 2
    
    key_peers = list(diccionario.keys())
    
    extra = 4
    
    
    for a in range(0,len(key_peers)):
        if diccionario[key_peers[a]] == []:
            extra = extra-1
            
        else:
            col = a + extra
            name = key_peers[a][0] + enter + key_peers[a][1] +enter + str(key_peers[a][2]) 
            
            sheet.update_cell(2, col, name)
        
    return('Peers agregados')

def names_row(diccionario):
    # Escribo los proveedores en la FILA 2
    
    key_peers = list(diccionario.keys())
    name_list = [] 
    
    
    
    for a in range(0,len(key_peers)):
        if diccionario[key_peers[a]] == []:
            pass
            
        else:
            name = key_peers[a][0] + enter + key_peers[a][1] +enter + str(key_peers[a][2]) 
            name_list.append(name)
            
    sheet.append_row(name_list, table_range='D2')
    
    return('Fila de peers escrita')
    
    
    



def first_void_row(column):
    row = 2
    value = sheet.cell(row,column).value
    while value != None:
        value = sheet.cell(row,column).value
        row += 1
    
    return(row - 1)


def first_void_column(row):
    column = 2
    value = sheet.cell(row,column).value
    while value != None:
        value = sheet.cell(row,column).value
        print(row,column)
        column += 1
    
    return(column-1)

def where_peer(peer):
    
    value = peer[0] + enter + peer[1] + enter + str(peer[2])
    
    location = str(sheet.find(value)).split()[1][-1]
    
    return(location)


def time_stamp():
    now = datetime.now()
    stamp = 'Última ejecución:  ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' - ' + str(now.hour) + ':' + str(now.minute)
    sheet.update_cell(1, 1, stamp)
    
    return('Estampa de tiempo enviada')
    

ppp = ('SILICA BACKUP WILD', '10.32.1.13', 7049)
'''
ver = where_peer(ppp)
print(ver)


ver = fill_peer_names(diccionario)
print(ver)


ver = time_stamp()
print(ver)


requests = {"requests": [{"updateCells": {"range": {"sheetId": sheet._properties['sheetId']}, "fields": "*"}}]}
res = sheet.batch_update(requests)
'''
# sheet.batch_update(data, kwarg

# https://understandingdata.com/python-for-seo/google-sheets-with-python/
'''
lista = sheet.col_values(5)
print(lista)

k = 0

while k < 42:

    sheet.append_row(['Test6', '', 'Test3',1,2,3,4,5,6,7,8,9,7,8,9,4,5,6,], table_range='A2')
    k += 1
    print(k)

#sheet.append_rows(5,{1:'23',2:'23'})
'''