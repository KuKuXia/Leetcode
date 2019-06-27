print(
    int(''.join(reversed(list(bin(0b00000010100101000001111010011100)[2:]))), 2))

for i in reversed(list(bin(0b00000010100101000001111010011100))):
    print(i)

a = list(reversed(list(bin(0b00000010100101000001111010011100))[2:]))
print(a)
a.append(['0' * (32 - len(a))])
print(a)
