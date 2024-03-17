def strengthHand(suits, cards):
  cardNums = numOfSameCards(cards)
  values = list(cardNums.values())
  keys = list(cardNums.keys())
  if checkStraight(cards) and checkFlush(suits) and cards[4] == 14:
    return [10, 0]
  elif checkStraight(cards) and checkFlush(suits):
    return [9, max(keys)]
  elif 4 in values:
    return [8, keys[values.index(4)], keys[values.index(1)]]
  elif 3 in values and 2 in values:
    return [7, keys[values.index(3)], keys[values.index(2)]]
  elif checkFlush(suits):
    ret = [6]
    for i in range(5):
      ret.append(cards[-(i+1)])
    return ret
  elif checkStraight(cards):
    return [5, max(keys)]
  elif 3 in values:
    keysCopy = keys.copy()
    keysCopy.remove(keys[values.index(3)])
    keysCopy.sort(key=None, reverse=True)
    return [4, keys[values.index(3)], *keysCopy]
  elif values.count(2) == 2:
    keysCopy = keys.copy()
    for i in range(3):
      if values[i] != 2:
        nonPairCard = keys[i]
        keysCopy.remove(keys[i])
        break
    keysCopy.sort(key=None, reverse=True)
    return [3, *keysCopy, nonPairCard]
  elif 2 in values:
    keysCopy = keys.copy()
    keysCopy.remove(keys[values.index(2)])
    keysCopy.sort(key=None, reverse=True)
    return [2, keys[values.index(2)], *keysCopy]
  return [1, *sorted(keys, key=None, reverse=True)]
def checkStraight(cards):
  if cards == [2, 3, 4, 5, 14]:
    return True
  for i in range(len(cards) - 1):
    if cards[i] + 1 != cards[i + 1]:
      return False
  return True
def checkFlush(suits):
  suit = suits[0]
  for i in range(len(suits) - 1):
    if suits[i + 1] != suit:
      return False
  return True
def numOfSameCards(cards):
  cardNums = {}
  for card in cards:
    if card in cardNums:
      cardNums[card] = cardNums[card] + 1
    else:
      cardNums[card] = 1
  return cardNums
def doNothin():
  pass

with open("poker.txt") as f:
  lines = f.readlines()
allHands = []
n = 0
for i in lines:
  n = n + 1
  hand = []
  p1suit = []
  p1card = []
  p2suit = []
  p2card = []
  l = i[:-1]
  if n == 1000:
    l = l + lines[-1][-1]
  l = l.split(" ")
  q = 0
  for r in l:
    q = q + 1
    if q < 6:
      p1suit.append(r[1])
      if r[0] == "T":
        p1card.append(10)
      elif r[0] == "J":
        p1card.append(11)
      elif r[0] == "Q":
        p1card.append(12)
      elif r[0] == "K":
        p1card.append(13)
      elif r[0] == "A":
        p1card.append(14)
      else:
        p1card.append(int(r[0]))
    elif q > 5:
      p2suit.append(r[1])
      if r[0] == "T":
        p2card.append(10)
      elif r[0] == "J":
        p2card.append(11)
      elif r[0] == "Q":
        p2card.append(12)
      elif r[0] == "K":
        p2card.append(13)
      elif r[0] == "A":
        p2card.append(14)
      else:
        p2card.append(int(r[0]))
  p1card.sort()
  p2card.sort()
  hand.append(p1suit)
  hand.append(p1card)
  hand.append(p2suit)
  hand.append(p2card)
  allHands.append(hand)

p1wins = 0
for foot in allHands:
  print(foot[0], foot[1], strengthHand(foot[0], foot[1]))
  if strengthHand(foot[0], foot[1])[0] > strengthHand(foot[2], foot[3])[0]:
    p1wins = p1wins + 1
  elif strengthHand(foot[0], foot[1])[0] == strengthHand(foot[2], foot[3])[0]:
    for i in range(len(strengthHand(foot[0], foot[1]))):
      if strengthHand(foot[0], foot[1])[i] > strengthHand(foot[2], foot[3])[i]:
        p1wins = p1wins + 1
        break
      elif strengthHand(foot[0], foot[1])[i] < strengthHand(foot[2], foot[3])[i]:
        break
print(p1wins)
