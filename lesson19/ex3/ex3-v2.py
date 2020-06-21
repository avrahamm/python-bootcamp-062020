"""
This solution assumes JSON format of hosts.json file
"""
import json
import sys

with open('hosts.json') as json_file:
    data = json.load(json_file)
    host_ip_dict = data['host_ip_dict']

print(host_ip_dict)

input_params = sys.argv[1:len(sys.argv)]
hosts = [host for host in input_params]

for host in hosts:
    try:
        print(f"{host}: {host_ip_dict[host]}")
    except KeyError:
        print(f"{host} does not exist")
