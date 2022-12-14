def isPalindrome(str):
    palcounter = 0
    for i in str:
        counter = 0
        x = str.find(i)
        if x != -1:
            while i in str:
                str = str.replace(i, ' ', 1)
                counter += 1
            if counter % 2 != 0:
                palcounter += 1
    if palcounter > 1:
        return False
    else:
        return True


print(isPalindrome("trueitrue"))
