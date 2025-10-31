def ip_to_binary(ip_address: str) -> str:
    return ''.join(f'{int(octet):08b}' for octet in ip_address.split('.'))

def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix = ip_cidr.split('/')
    binary_ip = ip_to_binary(ip)
    return binary_ip[:int(prefix)]
print(ip_to_binary("192.168.1.10"))
print(get_network_prefix("192.168.1.10/24"))

