print("""-Выберите язык:
0- Русский

-Selected language:
1- English

-Bir dil seçin:
2- Türk
""")
language = int(input())

while language != 0 and language != 1 and language != 2:
    print('Попробуйте еще раз | Try again | Tekrar deneyin')
    language = int(input())
else:
    if language == 0:
        import local_rus as lc
    elif language == 1:
        import local_eng as lc
    elif language == 2:
        import local_turc as lc

print(lc.HELLO)

hello = int(input())

while hello != 1 and hello != 2 and hello != 3 and hello != 4 and hello != 5 and hello != 6:
    print(lc.MISTAKE)
    hello = int(input())
else:
    if hello == 1:
        print(lc.FIRST)
    elif hello == 2:
        print(lc.SECOND)
    elif hello == 3:
        print(lc.THIRD)
    elif hello == 4:
        print(lc.FOUR)
    elif hello == 5:
        print(lc.FIVE)
    else:
        print(lc.SIX)
