"""
def caesar_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Example usage:
plaintext = "Hello, World!"
key = 3
encrypted_text = caesar_encrypt(plaintext, key)
print(f"Encrypted Text: {encrypted_text}")

"""
#Decryption
def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    for key in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")

# Example usage:
ciphertext = "FVDWDMP"
brute_force_caesar(ciphertext)
