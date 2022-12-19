def morse_number(n):
    a = []
    for i in n:
        if 0 < int(i) < 6:
            b = int(i) * '.'
            while len(b) < 5:
                b += '-'
            a.append(b)
        elif int(i) > 5:
            b = (int(i) - 5) * '-'
            while len(b) < 5:
                b += '.'
            a.append(b)
        else:
            a.append('-----')
    return ' '.join(a)

print(morse_number('295'))
print(morse_number('005'))
print(morse_number('513'))
print(morse_number('784'))
