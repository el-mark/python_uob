def caesar_cipher_encryption(raw_text, shift):
    new_text = ""
    for character in raw_text:
        ascii_ord = ord(character) - shift
        new_text += chr(ascii_ord)
        # if ascii_ord <= ord("z"):
        # else:
        #     readjust_distance = ord("z") - ord("a") + 1
        #     new_text += chr(ascii_ord - readjust_distance)
    return new_text

normal_file = open('encrypted.txt', 'r')
encrypted_file = open('final.txt', 'w')

shift = int(input("input a distance value: "))
for character in normal_file.read():
    encrypted_file.write(
        caesar_cipher_encryption(character, shift)
    )
encrypted_file.close()

# word = input("input a word: ")
# encrypted_word = caesar_cipher_encryption(word, shift)
# print(encrypted_word)

# print(ord("a")) => 97
# print(ord("z")) => 122
