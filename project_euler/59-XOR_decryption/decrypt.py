#the encryption key consists of three lower case characters
def xor_check(key, values):  #KEY is "nha" VALUES are [100,20,304,20]
  key_list = [ord(key[i]) for i in range(len(key))]
  final_list = []
  for count, value in enumerate(values):
    final_list.append(chr(int(value) ^ int(key_list[count % len(key)])))
  new_final_str = ""
  for char in final_list:
    new_final_str = new_final_str + char

  return new_final_str.split(" ")


from english_words import get_english_words_set

web2lowerset = get_english_words_set(['web2'], lower=True)


def check_for_english(words, ratio):
  count = 0
  for word in words:
    if word in web2lowerset:
      count += 1
  return count / len(words) > ratio


with open("0059_cipher.txt") as file:
  values = file.read().split(",")

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

count = 0

for key1 in ascii_lowercase:
  for key2 in ascii_lowercase:
    for key3 in ascii_lowercase:
      count += 1
      print(f"{count}", end="\r")
      key = key1 + key2 + key3
      words = xor_check(key, values)
      if check_for_english(words, 0.5):
        print(key)
        print(" ".join(words))
