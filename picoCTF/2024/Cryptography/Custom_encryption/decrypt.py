from random import randint

def decrypt(cipher_arr, key):
    plain_text = ""
    for num in cipher_arr:
        plain_text += chr(int(num / key / 311))
    return plain_text

def dynamic_xor_decrypt(cipher_text, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        plain_text += chr(ord(char) ^ ord(key_char))
    return plain_text[::-1]

if __name__ == '__main__':
    shared_key = 35
    text_key = "trudeau"
    cipher = [97965, 185045, 740180, 946995, 1012305, 21770, 827260, 751065, 718410, 457170, 0, 903455, 228585, 54425, 740180, 0, 239470, 936110, 10885, 674870, 261240, 293895, 65310, 65310, 185045, 65310, 283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]
    
    semi_cipher = decrypt(cipher, shared_key)
    plain_text = dynamic_xor_decrypt(semi_cipher, text_key)
    print(plain_text)