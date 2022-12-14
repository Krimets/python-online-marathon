def Cipher_Zeroes(N):
    zero_counter = 0
    for i in N:
        if i in '069':
            zero_counter += 1
        elif i == '8':
            zero_counter += 2
    if zero_counter == 0:
        zero_counter = 0
    elif zero_counter % 2 != 0:
        zero_counter += 1
    else:
        zero_counter -= 1
    return "{0:b}".format(zero_counter)


print(Cipher_Zeroes("565"))
print(Cipher_Zeroes("8200"))
print(Cipher_Zeroes("4900"))

print(Cipher_Zeroes("4"))