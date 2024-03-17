import random
sentences_counter = 0
mem = ""

chain = {}
print ("Pick a level. ", end = "")
level = int (input())
print ("Pick a file that ends in .txt. (type the file name) ", end = "")
file = input()
print ("How many sentences? ", end = "")
sentences_num = int(input())
with open(file) as f:
    key = f.read(level).upper()
    while True:
        ch = f.read(1).upper()
        if not ch:
            break
        if key not in chain:
            chain[key] = [ch]
        else:
            chain[key].append(ch)
        key = key[1:] + ch
key = random.choice(list(chain.keys()))
print(key, end = "")
while sentences_num > sentences_counter:
    ch = random.choice(chain[key])
    if ch == None:
        mem = key
        key = random.choice(list(chain.keys()))
        if key is not mem:
            ch = random.choice(chain[key])
    print(ch, end = "")
    key = key[1:] + ch
    if ch == "." or ch == "?" or ch == "!":
        sentences_counter += 1
    
        
        
    
