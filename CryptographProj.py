import random

Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 

# ------------------------------------------------------ MONOALPHABETIC CIPHER ------------------------------------------------------ #

def random_key(): 
    shuffled_alphabet = list(Alphabet)  
    random.shuffle(shuffled_alphabet)  
    
    key_pair = dict(zip(Alphabet, shuffled_alphabet))
    return key_pair


key_pair = random_key()

def text_to_mono(text):
    mono_code = []
    for char in text.upper():
        if char in key_pair:
            mono_code.append(key_pair[char])
        else:
            mono_code.append(' ') 
    return ' '.join(mono_code)

def mono_to_text(mono):

    mono_code_list = mono.split(' ')
    text = []
    for code in mono_code_list:
        if code in key_pair.values():
            text.append(list(key_pair.keys())[list(key_pair.values()).index(code)])
        else: 
            text.append(' ') 
    return ' '.join(text)

# ------------------------------------------------------ CAESAR CIPHER ------------------------------------------------------ #

def caesar_cipher(text, shift):
    result = ''

    for char in text:
        if char in Alphabet:
            new_index = (Alphabet.index(char) + shift) % 26
            result += Alphabet[new_index]
        else:
            result += char

    return ''.join(result)



# ------------------------------------------------------ MORSE CODE ------------------------------------------------------ #

# Dictionary mapping each letter to its Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}  # Reverse the dictionary

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            if char.isdigit():
                # Increment the number by 3 and wrap around if necessary
                new_num = str((int(char) + 3) % 10)
                morse_code.append(MORSE_CODE_DICT[new_num])
            else:
                morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')  # If the character is not in the dictionary add a space
    return ' '.join(morse_code)

def morse_to_text(morse):
    # Split the morse code by spaces to handle each letter or word
    morse_code_list = morse.split(' ')
    text = []
    for code in morse_code_list:
        if code in REVERSE_MORSE_CODE_DICT:
            char = REVERSE_MORSE_CODE_DICT[code]
            if char.isdigit():
                # Decrement the number by 3 and wrap around if necessary
                new_num = str((int(char) - 3) % 10)
                text.append(new_num)
            else:
                text.append(char)
        else:
            text.append(' ')  # If the Morse code doesn't exist in the dictionary add a space
    return ''.join(text)


# ------------------------------------------------------ VIGENERE CIPHER ------------------------------------------------------ #


def vigenere_encrypt(text, key):
    encrypted_text = []
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char in Alphabet:
            shift = Alphabet.index(key[key_index])
            new_index = (Alphabet.index(char) + shift) % 26
            encrypted_text.append(Alphabet[new_index])
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text.append(char)  

    return ''.join(encrypted_text)


def vigenere_decrypt(text, key):
    decrypted_text = []
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char in Alphabet:
            shift = Alphabet.index(key[key_index])
            new_index = (Alphabet.index(char) - shift) % 26
            decrypted_text.append(Alphabet[new_index])
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text.append(char)  

    return ''.join(decrypted_text)


# ------------------------------------------------------ MAIN FUNCTION ------------------------------------------------------ #

def main():
    
    while True:

        Choice = int(input("What Encryption Would you like your message to be encrypted with? \n"
                           "1. Caesar Cipher \n"
                           "2. Monoalphabetic Cipher \n"
                           "3. Vigenere Cipher \n"
                           "4. Morse Code \n"
                           "5. Decrypt \n"
                           "6. Exit \n"))

        if Choice == 1:
            print("Caesar Cipher")
            message = input("Please Enter a Message to Encrypt: ")
            shift = int(input("Enter the shift value: "))

            print(f"Original Alphabet: \n{Alphabet}")
            print(f"Caesar Cipher Alphabet : \n{list(caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', shift))}\n")
            print(f"Encrypted Message :\n{caesar_cipher(message.upper(), shift)}")

            while True:

                print("Would you like to decrypt the message?")
                decrypt = input("(1) Yes or (0)No : ")
                if decrypt == "1":
                    message = input("Please Enter a Message to Decrypt: ")
                    print(caesar_cipher(message.upper(), -shift) + "\n")
                elif decrypt == "0":
                    print("Goodbye")
                    break


        elif Choice == 2:   
            print("Monoalphabetic Cipher")
            message = input("Please Enter a Message to Encrypt: ")

            print("Original Alphabet:", Alphabet)
            print("Shuffled Alphabet:", list(key_pair.values()))

            print(f"Encrypted Message :\n{text_to_mono(message)}")

            while True:

                print("Would you like to decrypt the message?")
                decrypt = input("(1) Yes or (0)No : ")
                if decrypt == "1":
                    message = input("Please Enter a Message to Decrypt: ")
                    print(mono_to_text(message) + "\n")
                elif decrypt == "0":
                    print("Goodbye")
                    break


        elif Choice == 3:
            print("Vignere Cipher")
            message = input("Please Enter a Message to Encrypt: ")
            key = input("Enter the key: ")

            print(f"Encrypted Message :\n{vigenere_encrypt(message, key)}")

            while True:
                print("Would you like to decrypt the message?")
                decrypt = input("(1) Yes or (0)No : ")
                if decrypt == "1":
                    message = input("Please Enter a Message to Decrypt: ")
                    key = input("Enter the key: ")
                    print(vigenere_decrypt(message, key) + "\n")
                elif decrypt == "0":
                    print("Goodbye")
                    break


        elif Choice == 4:
            print("\nMorse Code")
            message = input("Enter a Message to Encrypt: ")
            key = input("Enter Key: ")
            encrypted_msg1 = vigenere_encrypt(message, key)
            encrypted_msg2 = text_to_morse(encrypted_msg1)
            print(f"Encrypted Message: {encrypted_msg2}")

            decrypt = input("\nDecrypt message? (1) Yes or (0) No: ")
            if decrypt == "1":

                decrypted_msg1 = morse_to_text(encrypted_msg2)
                decrypted_msg2 = vigenere_decrypt(decrypted_msg1, key)
                print(f"Decrypted Message: {decrypted_msg2}\n")

        elif Choice == 6:
            print("Goodbye")
            exit()
        elif Choice == 5:
            while True:
                Choice2 = int(input("What Decryption Would you like your message to be Decrypted with? \n"
                        "1. Caesar Cipher \n"
                        "2. Monoalphabetic Cipher \n"
                        "3. Vigenere Cipher \n"
                        "4. Morse Code Modified \n"
                        "5. Exit \n"))
                if Choice2 == 1:
                    message = input("Please Enter a Message to Decrypt: ")
                    print(caesar_cipher(message.upper(), -shift) + "\n")

                elif Choice2 == 2:
                    message = input("Please Enter a Message to Decrypt: ")
                    print(mono_to_text(message) + "\n")
                elif Choice2 == 3:
                        message = input("Please Enter a Message to Decrypt: ")
                        key = input("Enter the key: ")
                        print(vigenere_decrypt(message, key) + "\n")

                elif Choice2 == 4:
                    message = input("Enter a Message to Encrypt: ")
                    key = input("Enter Key: ")
                    decrypted_msg1 = morse_to_text(message)
                    decrypted_msg2 = vigenere_decrypt(decrypted_msg1, key)
                    print(f"Decrypted Message: {decrypted_msg2}\n")
                elif Choice2 == 5:
                    print("Exiting Decryption...")
                    break
        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()
