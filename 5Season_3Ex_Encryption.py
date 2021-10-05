text = input('Enter string: ')
enc_char = ''
enc_char_list = []

# Encryption
for char in text:
    enc_char = ord(char) + 12 
    enc_char_list.append(enc_char)

print(enc_char_list)

# Decryption
for digit in enc_char_list:
    dec_digit = chr(digit -12)
    print(dec_digit, end= '')
print()
    
