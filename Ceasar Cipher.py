import string

def caesar_cipher(text, shift, encrypt=True):
    alphabet = string.ascii_letters
    if encrypt:
        shifted = alphabet[shift:] + alphabet[:shift]
    else:
        shift = -shift
        shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    return text.translate(table)


while True:
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice.lower() == 'q':
        break
    elif choice.lower() == 'e':
        plaintext = input("Enter the plaintext: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher(plaintext, shift, encrypt=True)
        print("Encrypted text:", encrypted_text)
    elif choice.lower() == 'd':
        encrypted_text = input("Enter the encrypted text: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_cipher(encrypted_text, shift, encrypt=False)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please try again.")

