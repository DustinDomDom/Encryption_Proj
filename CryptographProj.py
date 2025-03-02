import random

Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # List of all the letters in the alphabet in array form

# ------------------------------------------------------ MONOALPHABETIC CIPHER ------------------------------------------------------ #

def random_key():  # Random key generator
    shuffled_alphabet = list(Alphabet)  
    random.shuffle(shuffled_alphabet)  
    
    # Create a dictionary that maps each letter of the original alphabet to the shuffled alphabet
    key_pair = dict(zip(Alphabet, shuffled_alphabet))
    return key_pair


key_pair = random_key()

def text_to_mono(text):
    mono_code = []
    for char in text.upper():
        if char in key_pair:
            mono_code.append(key_pair[char])
        else:
            mono_code.append(' ')  # If the character is not in the dictionary add a space
    return ' '.join(mono_code)

def mono_to_text(mono):
    # Split the mono code by spaces to handle each letter or word
    mono_code_list = mono.split(' ')
    text = []
    for code in mono_code_list:
        if code in key_pair.values():
            text.append(list(key_pair.keys())[list(key_pair.values()).index(code)])
        else: 
            text.append(' ')  # If the mono code doesn't exist in the dictionary add a space
    return ''.join(text)



# ------------------------------------------------------ CAESAR CIPHER ------------------------------------------------------ #

def caesar_cipher(text, shift): # Caesar Cipher function
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
            text.append(REVERSE_MORSE_CODE_DICT[code])
        else: 
            text.append(' ')  # If the Morse code doesn't exist in the dictionary add a space
    return ''.join(text)


def main():
    
    while True:

        Choice = int(input("What Encryption Would you like your message to be encrypted with? \n"
                           "1. Caesar Cipher \n"
                           "2. Monoalphabetic Cipher \n"
                           "3. ? \n"
                           "4. Morse Code \n"
                           "5. Exit \n"))

        if Choice == 1:
            print("Caesar Cipher")
            message = input("Please Enter a Message to Encrypt: ")
            shift = int(input("Enter the shift value: "))

            print(f"Original Alphabet: \n{Alphabet}")
            print(f"Caesar Cipher Alphabet : \n{list(caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', shift))}\n")
            print(f"Encrypted Message :\n{caesar_cipher(message.upper(), shift)}")

            print("Would you like to decrypt the message?")
            decrypt = input("(1) Yes or (0)No : ")
            if decrypt == "1":
                message = input("Please Enter a Message to Decrypt: ")
                print(caesar_cipher(message.upper(), -shift) + "\n")
            elif decrypt == "0":
                print("Goodbye")


        elif Choice == 2:   
            print("Monoalphabetic Cipher")
            message = input("Please Enter a Message to Encrypt: ")

            print("Original Alphabet:", Alphabet)
            print("Shuffled Alphabet:", list(key_pair.values()))

            print(f"Encrypted Message :\n{text_to_mono(message)}")

            print("Would you like to decrypt the message?")
            decrypt = input("(1) Yes or (0)No : ")
            if decrypt == "1":
                message = input("Please Enter a Message to Decrypt: ")
                print(mono_to_text(message) + "\n")
            elif decrypt == "0":
                print("Goodbye")


        elif Choice == 3:
            print("3")


        elif Choice == 4:
            print("Morse Code")
            message = input("Please Enter a Message to Encrypt: ")
            print(text_to_morse(message))

            print("Would you like to decrypt the message?")
            decrypt = input("(1)Yes or (0)No : ")
            if decrypt == "1":
                message = input("Please Enter a Message to Decrypt: ")
                print(morse_to_text(message) + "\n")
            elif decrypt == "0":
                print("Goodbye")

        elif Choice == 5:
            print("Goodbye")
            exit()

        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()
