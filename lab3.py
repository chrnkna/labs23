words=[]
while( word:=str(input())) !="stop":
    words.append(word)
print(" ".join(words))


def z2():
    slova=[]
    while (new_word:=str(input()))!="stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else: print("Это не очень редкое слово... ")


def z3():
    from random import randint
    c = 0
    d = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a}+{b} = ", end="")
        res = input()

        while not res.isdigit() and res != "stop":
            print("Ответ не верный")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            d += 1
            print("Правильно!")
        else:
            print("Ответ неверный ")
            c += 1
        if c >= 3:
            print("Игра окончена.Правильных ответов =", d)

z2(),z3()