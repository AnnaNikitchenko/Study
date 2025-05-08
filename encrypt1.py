def caesar_encrypt(message, key):
    result = ""
    encrypt_text = ""
    for character in message:
        if 'a' <= character <= 'z':
            start = ord('a')
            encrypt_text = chr((ord(character) + key - start) % 26 + start)
        elif 'A' <= character <= 'Z':
            start = ord('A')
            encrypt_text = chr((ord(character) + key - start) % 26 + start)
        else:
            encrypt_text = character
        result += encrypt_text
    return result


key = 1
message = "The quick brown fox jumps over the lazy dog."
print(caesar_encrypt(message, key))
