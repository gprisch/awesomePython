def ip_dec_to_bin(ip_dec: str, radix=2):
    return '.'.join([f'{int(n):08b}' for n in ip_dec.split('.')])


an_ip = '192.168.1.12'
print(ip_dec_to_bin(an_ip))

s = '12'
assert s.zfill(7) == '0000012'

# functions
a_bin = bin(192)
a_oct = oct(192)
a_hex = hex(192)
print("192: b:%s o:%s h:%s" % (a_bin, a_oct, a_hex))

assert int(0b11000000) == 192
assert int(0o300) == 192
assert int(0xc0) == 192

# recall of the bitwise and bitshift operators
an_ip = '192.168.0.1'
subnet_mask = '255.255.255.0'
cidr = 26
byte, mod = divmod(cidr, 8)
print(byte, mod, sep=' ')

