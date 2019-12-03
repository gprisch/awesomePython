user_input = '192.168.1.12'
ip = '.'.join([f'{int(n):08b}' for n in user_input.split('.')])
print(ip)