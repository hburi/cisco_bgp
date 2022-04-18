#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Abril 2022
Autor: Héctor Fernando Buri

Relevamiento automático de redes publicadas en neighbors BGP - CISCO
"""

#https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c

from funciones_cisco import conn_command, net_finder, name_finder, ip_finder, only_number_finder
from funciones_sheet import write_rows

enter = '\n'
# Pigué

ip = '******'
port = '******'
user = '******'
password = '******'
'''

# San josé

ip = '******'
port = '******'
user = '******'
password = '******'
'''

comm_neigh = 'show ip bgp neighbors'
filt_desc =  " | i Desc"

filt_numbers =  " | i BGP neighbor is"
#comando_1 = 'show ip bgp neighbors' + enter



bgp_names = conn_command(ip,user,password,port,comm_neigh + filt_desc)
bgp_numbers = conn_command(ip,user,password,port,comm_neigh + filt_numbers)


#print(bgp_numbers)

names = list(map(name_finder,bgp_names))
names = [name for name in names if name != '']

peer_ip = list(map(ip_finder,bgp_numbers)) 
peer_ip = peer_ip[-(len(names)):]

peer_as = list(map(only_number_finder,bgp_numbers))
peer_as = peer_as[-(len(names)):]

#peer_as = peer_as[1:len(peer_as)]
#print(enter.join(map(str, bgp_names)))
#print(enter.join(map(str, bgp_numbers)))
#print(list(names))
#print(list(peer_ip),'****')


#print(len(peer_as))
#print(len(peer_ip))


net_dict = {}
as_and_ip = []
key = ()

for index in range(0,len(peer_ip)):
    if peer_ip[index] == []:
        pass
    else:
        #print(names[index],peer_ip[index],peer_as[index])
        show_adver = 'show ip bgp neighbors ' + peer_ip[index][0] + ' advertised-routes'
        nets = conn_command(ip,user,password,port, show_adver)
        nets_string = ''.join(nets)
        clean_nets = net_finder(nets_string)
        #print(clean_nets)

        key = (names[index],peer_ip[index][0],int(peer_as[index][0][:-1]))
        
        net_dict[key] = clean_nets 


print (net_dict)


write_rows(net_dict)
