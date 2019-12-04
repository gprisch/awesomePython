user_input = '192.168.1.12'
ip = '.'.join([f'{int(n):08b}' for n in user_input.split('.')])
print(ip)

# functions
a_bin = bin(192)
a_oct = oct(192)
a_hex = hex(192)
print("192: b:%s o:%s h:%s" % (a_bin, a_oct, a_hex))

print(int(0b11000000))
print(int(0o300))
print(int(0xc0))