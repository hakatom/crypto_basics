def repeating_key_xor(string,key):
    print(type(key),type(string))
    key_length=len(key)
    xored_key=[]
    for index,item in enumerate(string):
        print(index)
        xored_key.append(string[index]^key[index%key_length])
    return bytes(xored_key)

def main():
    string="Burning 'em, if you ain't quick and nimble" \
           "I go crazy when I hear a cymbal"
    key="ICE"

    print(repeating_key_xor(string.encode(),key.encode()).hex())

if __name__ == "__main__":
    main()