

encrypted_flag = open('output.txt').read()
ciphertext = encrypted_flag.split('\n')[3].split(' ')[:-1]


for encrypted_char in ciphertext:
    encrypted_char = int(encrypted_char)
    
    decrypted_char = chr(round(encrypted_char ** (1/3)))
    print(decrypted_char, end='')