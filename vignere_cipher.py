def generate_key(message, key):
    key = list(key) #converts the key to a list
    expanded_key = [] #list to store the expanded version of the key
    i = 0
    for char in message: #iterates through each character in the message
        if char.isalpha():  #if the character is a letter
            expanded_key.append(key[i % len(key)]) #appends the corresponding key character
            i += 1
        else:
            expanded_key.append(char) #appends non-alphabetic characters
    return "".join(expanded_key) #joins the list of characters into a string


def encrypt(message: str, key: str) -> str:
    encrypted_message = [] #list to store the encrypted message
    for i in range(len(message)):  #iterates through each character in the message
        if message[i].isalpha():  #if the character is a letter
            if message[i].isupper(): #if the character is uppercase
                shift = ord('A') #calculates the ASCII value of 'A'
            else:
                shift = ord('a') #calculates the ASCII value of 'a'
            val = (ord(message[i]) - shift + ord(key[i].upper()) - ord('A')) % 26 #calculates the ASCII value of the encrypted character
            encrypted_message.append(chr(val + shift)) #converts the ASCII value to a character and appends it to the list
        else:
            encrypted_message.append(message[i])  #appends non-alphabetical characters
    return "".join(encrypted_message)  #joins the list of characters into a string


def decrypt(message: str, key: str) -> str:
    decrypted_message = [] #list to store the decrypted message
    for i in range(len(message)):  #iterates through each character in the message
        if message[i].isalpha():  #if the character is a letter
            if message[i].isupper(): #if the character is uppercase
                shift = ord('A') #calculates the ASCII value of 'A'
            else:
                shift = ord('a') #calculates the ASCII value of 'a'
            val = (ord(message[i]) - shift - (ord(key[i].upper()) - ord('A')) + 26) % 26 #calculates the ASCII value of the decrypted character
            decrypted_message.append(chr(val + shift)) #converts the ASCII value to a character and appends it to the list
        else:
            decrypted_message.append(message[i])  #appends non-alphabetical characters
    return "".join(decrypted_message)  #joins the list of characters into a string
