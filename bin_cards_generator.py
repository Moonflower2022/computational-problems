import math

# 60 and 30 are good

numbers = 60
cardsNum = math.ceil(math.log(numbers, 2))
cards = []
for i in range(cardsNum):
    cards.append([])

for i in range(numbers):
    n = i + 1
    binNum = bin(n)[2:]
    for o in range(cardsNum):
        if o < len(binNum) and binNum[-(o+1)] == "1":
            cards[o].append(n)


for i in range(cardsNum):
    print(cards[i])
print(cards)

print(cardsNum)

for i in range(cardsNum):
    print(len(cards[i]))
