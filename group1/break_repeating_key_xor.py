import single_byte_xor
# from Fixed_Xor import bytes_xor
# #
# #
# # def get_hamming_distance(bin_str1,bin_str2):
# #     diff=0
# #     for byte in bytes_xor(b1,b2):
# #         diff+=bin(byte).count('1')
# #     return diff
def get_hamming_distance(x,y):
    return sum([bin(x[i]^y[i]).count('1')for i in range(len(x))])



b1=bytes('this is a test','utf8')
b2=bytes('wokka wokka!!!','utf8')

print(get_hamming_distance(b1,b2))

def get_keylength_with_shortest_distance(str1):
    lengths=[]
    for keylength in range(2,41):
        b1=str1[:keylength]
        b2=str1[keylength:keylength*2]
        b3=str1[keylength*2:keylength*3]
        b4=str1[keylength*3:keylength*4]
        normalized_distance=float((get_hamming_distance(b1,b2)+get_hamming_distance(b2,b3)+get_hamming_distance(b3,b4))/keylength*3)
        lengths.append(keylength,normalized_distance)

    lengths=sorted(lengths,key=lambda x:x[1], reverse=True)
    return lengths[0]

def break_repeating_key_xor(keylength,ciphertext):
    block_bytes=[[] for _ in range(keylength)]
    for i, byte in enumerate(b):
        block_bytes[i%keylength].append(byte)

    keys=''
    for bbytes in block_bytes:
        keys+=single_byte_xor.get_best_score(bbytes)

    key=bytearray(keys)



#print(get_hamming_distance(bytearray('this is a test'.encode()),bytearray('wokka wokka!!!'.encode())))