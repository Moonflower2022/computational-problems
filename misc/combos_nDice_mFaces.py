print("This is a program made to calculate the number of ways you can get to a sum of numbers (m) by rolling n d6 dice")
print("for example, enter # of dice as 2 and total from those dice as 2 and since there is only one way to get a total of two from two dice the answer should be 1")
print("--------------------------------------------------------")


def user_input():
    print("# of dice?(integer) ")
    n = int(input())
    print("total from those dice?(integer) ")
    m = int(input())
    lookup = []
    for i in range(n):
        lookup.insert(i, [])
        for o in range(m):
            if i == 0:
                if o <= 5 and o >= 0:
                    lookup[i].insert(o, 1)
                else:
                    lookup[i].insert(o, 0)
            else:
                num = 0
                for s in range(6):
                    if lookup[i - 1][o - s - 1]:
                        num = num + lookup[i - 1][o - s - 1]
                lookup[i].insert(o, num)
    print("OUTPUT")
    print(lookup[i][o])
    print("Table:")
    list = []
    for o in range(m):
        if len(str(o+1)) > 1:
            list.append(str(o+1))
        else:
            list.append(str(o+1) + " ")
    print(*["  ", *list])
    for i in range(len(lookup)):
        print(f"{i + 1} {lookup[i]}")
    user_input()


user_input()
