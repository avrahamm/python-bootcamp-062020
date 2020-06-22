"""
This solution assumes JSON format of hosts.json file
"""
import json
import sys

with open('hosts.json') as json_file:
    data = json.load(json_file)
    host_ip_dict = data['host_ip_dict']

print(host_ip_dict)

# I think this works the same way
# without an extra variable and without the
# list comprehension
hosts = sys.argv[1:]

for host in hosts:
    try:
        print(f"{host}: {host_ip_dict[host]}")
    except KeyError:
        print(f"{host} does not exist")
