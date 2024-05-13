

def decryptC3(cipher_text, lookup1, lookup2):
    plain_text = ""

    differences = []
    for char in cipher_text:
        differences.append(lookup2.index(char))
    
    first = differences[0]
    
    indexes = [first]
    for i, difference in enumerate(differences):
        if i != 0:
            indexes.append((indexes[i - 1] + difference) % 40)

    for index in indexes:
       plain_text += lookup1[index]

    return plain_text

if __name__ == '__main__':
    with open("Cryptography/C3/ciphertext", "r") as file:
        lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
        lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

        cipher_text = file.read()
        semi_cipher = decryptC3(cipher_text, lookup1, lookup2)

        print(semi_cipher)

        plain_text = ""
        num = 1
        for i, char in enumerate(semi_cipher):
            if i == num ** 3:
                plain_text += char
                num += 1

        print(plain_text)            





    


