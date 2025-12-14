import string

alphabet = string.ascii_lowercase


def cipher(word, shift):
    result = ""
    for char in word:
        if char in alphabet:
            old_index = alphabet.find(char)
            new_index = (old_index + shift) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result

word = input("Write a word: ").lower()
shift = int(input("Write a shift number: "))
encoded = cipher(word, shift)
print(encoded)

def decipher(word, shift):
    result = ""
    for char in word:
        if char in alphabet:
            old_index = alphabet.find(char)
            new_index = (old_index - shift) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result

decoded = (decipher(encoded, shift))
print(decoded)

