import sys

host_ip_dict = {}
with open('hosts', 'r') as f:
    for line in f:
        parts = line.split("=")
        host_ip_dict[parts[0]] = parts[1].strip()

print(host_ip_dict)

hosts = sys.argv[1:]

for host in hosts:
    try:
        print(f"{host}: {host_ip_dict[host]}")
    except KeyError:
        print(f"{host} does not exist")
