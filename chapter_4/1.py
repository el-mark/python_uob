def caesar_cipher_encryption(raw_text, shift):
    new_text = ""
    for character in raw_text:
        ascii_ord = ord(character) + shift
        if ascii_ord < ord("z"):
            new_text += chr(ascii_ord)
        else:
            print(ascii_ord)
            print(ascii_ord - 122)
            readjust_distance = ord("z") - ord("a") + 1
            new_text += chr(ascii_ord - readjust_distance)
    return new_text

word = input("input a word: ")
shift = int(input("input a distance value: "))
encrypted_word = caesar_cipher_encryption(word, shift)
print(encrypted_word)

# print(ord("a")) => 97
# print(ord("z")) => 122
