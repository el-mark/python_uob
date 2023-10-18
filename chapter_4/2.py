def caesar_cipher_decryption(raw_text, shift):
    new_text = ""
    for character in raw_text:
        ascii_ord = ord(character) - shift
        if ascii_ord >= ord("a"):
            new_text += chr(ascii_ord)
        else:
            readjust_distance = ord("z") - ord("a") + 1
            new_text += chr(ascii_ord + readjust_distance)
    return new_text

word = input("input a word: ")
shift = int(input("input a distance value: "))
encrypted_word = caesar_cipher_decryption(word, shift)
print(encrypted_word)
