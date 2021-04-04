alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
# word = 'ljes=njak'
count = 0
for i in range(len(alphabet)):
    while alphabet[i] in word:
        word = word.replace(alphabet[i], " ", 1)
        # print(word)
        count += 1
        # print(count)

word = ''.join(word.split())
# print(word)
count += len(word)
print(count)