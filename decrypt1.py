key = 1
encrypted_message = "Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph."


def caesar_decrypt(encrypted_message, key):
    result = ''
    decrypt_text = ''
    for character in encrypted_message:
        if 'a' <= character <= 'z':
            start = ord('a')
            decrypt_text = chr((ord(character) - key - start) % 26 + start)
        elif 'A' <= character <= 'Z':
            start = ord('A')
            decrypt_text = chr((ord(character) - key - start) % 26 + start)
        else:
            decrypt_text = character
        result += decrypt_text
    return result


print(caesar_decrypt(encrypted_message, key))
