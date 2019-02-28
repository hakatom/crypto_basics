
def fixed_xor(a,b):
    result = int(a, 16) ^ int(b, 16)
    return '{:x}'.format(result)

def bytes_xor(b1,b2):
    assert len(b1)==len(b2)
    l=len(b1)
    b=bytearray(l)
    for i in range(l):
        b[i]=b1[i]^b2[i]
    return b

a="1c0111001f010100061a024b53535009181c"
b="686974207468652062756c6c277320657965"
a1=bytearray.fromhex(a)
b1=bytearray.fromhex(b)

be=bytes(bytes_xor(a1,b1))

#print (bytes_xor(a.encode(),b.encode()))