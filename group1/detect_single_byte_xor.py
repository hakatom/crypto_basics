import single_byte_xor

def brute_force_solve(input_hextring):
    best_scores=[]
    for line in input_hextring:
        hexline=bytes.fromhex(line)
        best_score=single_byte_xor.get_best_score(hexline)
        best_scores.append(best_score)
    abs_best=sorted(best_scores,key=lambda x:x['score'],reverse=True)[0]
    return abs_best

def main():
    input_file=open('4.txt')
    input_hextring=input_file.readlines()
    abs_bast=brute_force_solve(input_hextring)
    for item in abs_bast:
        print("{}: {}".format(item.title(), abs_bast[item]))

if __name__ == '__main__':
    main()
#input_ciphertext=bytes.fromhex(input_hextring)
