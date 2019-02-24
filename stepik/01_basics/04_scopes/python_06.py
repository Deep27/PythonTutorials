def f():
    ok_status = True
    vowels = ["a", "u", "i", "e", "o"]

    def check(word):
        nonlocal ok_status  # not global !!!
        for vowel in vowels:
            if vowel in word:
                return True
        ok_status = False
        return False

    print(check("abcaba"))
    print(ok_status)
    print(check("www"))
    print(ok_status)


f()
print(ok_status)  # NameError
