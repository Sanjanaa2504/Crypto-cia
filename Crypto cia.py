# Caesar Cipher Implementation with Hashing

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # If decrypt, reverse shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            base = ord('A') if char.isupper() else ord('a')

            # Shift character
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Keep spaces/symbols unchanged
            result += char

    return result


# Simple Hash Function
def simple_hash(text):
    hash_value = 0

    for i, char in enumerate(text):
        hash_value += (i + 1) * ord(char)

    return hash_value


if __name__ == "__main__":
    message = "Hello World"
    shift = 3

    print("Original Message:", message)

    # Encrypt
    encrypted = caesar_cipher(message, shift, "encrypt")
    print("Encrypted Message:", encrypted)

    # Hash of original
    original_hash = simple_hash(message)
    print("Original Hash:", original_hash)

    # Decrypt
    decrypted = caesar_cipher(encrypted, shift, "decrypt")
    print("Decrypted Message:", decrypted)

    # Hash of decrypted
    decrypted_hash = simple_hash(decrypted)
    print("Decrypted Hash:", decrypted_hash)

    # Verify Integrity
    if original_hash == decrypted_hash:
        print("Integrity Verified: Message is unchanged")
    else:
        print("Integrity Check Failed")