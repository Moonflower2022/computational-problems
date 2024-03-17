import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(encoded):
	plain = ""
	for i in range(0, len(encoded), 2):
		plain += chr(int("{0:04b}".format(ALPHABET.index(encoded[i])) + "{0:04b}".format(ALPHABET.index(encoded[i+1])), 2))
	return plain

def deshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

plaintext = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

for key in ALPHABET:
	decoded = ""
	for i, c in enumerate(plaintext):
		decoded += deshift(c, key[i % len(key)])
	print("key: " + key)
	print("output: " + b16_decode(decoded))
