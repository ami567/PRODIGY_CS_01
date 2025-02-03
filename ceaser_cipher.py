mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
s = int(input("Enter the shift value: "))



def encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Keeps non-alphabet characters unchanged

    return result


def decrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char  # Keeps non-alphabet characters unchanged

    return result


if mode == 'e':
    text = input("Enter the text to encrypt: ")
    print("Encrypted Text: ", encrypt(text, s))
elif mode == 'd':
    text = input("Enter the cipher text to decrypt: ")
    print("Decrypted Text: ", decrypt(text, s))
else:
    print("Invalid mode selected. Please choose 'E' or 'D'.")