text = input('Enter string: ')
nums = []

for char in text:
    nums.append(str(ord(char)+12))
# print(nums)
# ['84', '113', '120', '120', '123', '44', '128', '116', '117', '127', '44', '76', '76', '76', '62']

secret_text = ','.join(nums)
# print(secret_text)
# 84,113,120,120,123,44,128,116,117,127,44,117,127,44,76,76,76

string_list = []
for char in secret_text.split(','):
    string_list.append(chr(int(char)-12))
# print(string_list)
# ['H', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', '@', '@', '@']
print(''.join(string_list))
