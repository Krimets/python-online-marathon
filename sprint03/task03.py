def create_account(user_name: str, password: str, secret_words: list):
    special = '!_*'
    special_counter = 0
    for _ in special:
        if _ in password:
            special_counter += 1
    if special_counter == 0:
        raise ValueError
    if len(password) < 6:
        raise ValueError

    def check(pas, words):
        counter = 0
        s = [x for x in words]
        if pas != password:
            k = False
        elif len(s) != len(secret_words):
            k = False
        else:
            k = True
            for i in s:
                if s.count(i) > 2:
                    k = False
                elif i in secret_words:
                    counter += 1
            if k != False:
                if len(secret_words) - counter > 1:
                    k = False
                else:
                    k = True
        return k
    return check

tom = create_account("Tom", "Qwerty1_", ["1", "word"])
print(tom("Qwerty1_", ["1", "word"]))
print(tom("Qwerty1_", ["word"]))
print(tom("Qwerty1_", ["word", "2"]))
print(tom("Qwerty1!", ["word", "12"]))
