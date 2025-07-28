import ipaddress

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)
    print(f"{ip} is a valid IPv4 address.")
except ValueError:
    print(f"{ip} is NOT a valid IP address.")
