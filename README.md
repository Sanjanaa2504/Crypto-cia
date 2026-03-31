# Caesar_Cipher

Caesar Cipher implementation with hashing for integrity verification.

## Overview
This project demonstrates a basic Caesar Cipher algorithm used for encryption and decryption. It also includes a simple hashing function to verify that the decrypted message matches the original.

## Features
- Encrypt text using Caesar Cipher
- Decrypt encrypted text
- Handles uppercase and lowercase letters
- Ignores non-alphabet characters
- Includes hash-based integrity check

## How It Works

### Encryption
Each character is shifted forward by a fixed number.

Example:
HELLO → KHOOR (shift = 3)

### Decryption
Reverse the shift applied during encryption.

### Hashing
- Convert each character to ASCII
- Multiply by position
- Sum all values

## Usage

Run the program:
python caesar_cipher.py

## Example Output

Original Message: Hello World  
Encrypted Message: Khoor Zruog  
Decrypted Message: Hello World  
Integrity Verified

## Formula

Encryption:
E(x) = (x + shift) % 26

Decryption:
D(x) = (x - shift) % 26

## Limitations
- Not secure for real-world use
- Easily breakable

## Author
Sanjanaa Shree C H
