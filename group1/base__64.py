from codecs import encode
import binascii
#trn hex string to bytes:
base_64_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def based_64_encode(int_arr):
    result=""
    padding=""
    sz=len(int_arr)
    mod=sz%3
    if mod>0:
        for i in range(mod):
            padding+="="
            int_arr+='\0'

    for i in range(0,sz,3):

        if (mod>0) and (((mod/3)*4)%76==0):
            result+='\r\n'
        n=(int_arr[i]<<16)+(int_arr[i+1]<<8)+(int_arr[i+2])
        n1=(n>>18)&63
        n2=(n>>12)&63
        n3=(n>>6)&63
        n4=n&63

        result+="" + base_64_chars[n1]+base_64_chars[n2]+base_64_chars[n3]+base_64_chars[n4]
    rp=len(result)-len(padding)
    print(result)
    return result[0:rp:]+padding

based_64_encode(binascii.unhexlify("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))