# Caesar Cipher

The Caesar Cipher is a classic substitution cipher where each letter in the plaintext is shifted by a certain number of places down or up the alphabet. It is one of the oldest and simplest encryption techniques. Named after Julius Caesar, who used it to communicate securely with his officials, the cipher is a basic form of encryption that shifts characters in the alphabet.

<h3>How It Works</h3>

    
    For example, if we have a shift of 3:
        A becomes D
        B becomes E
        C becomes F
        And so on.



Example:

    Plaintext: HELLO
    Shift: 3
    Ciphertext: KHOOR

<h3>Formula:</h3>


<h4>For encryption:</h4>

Encrypted character = (Plaintext character + Shift) % 26


<h4>For decryption:</h4>

Decrypted character = (Ciphertext character - Shift) % 26

Where the alphabet is considered circular (i.e., after 'Z' it returns to 'A').

<h3>Features</h3>

    Encrypts text using the Caesar Cipher.
    Decrypts ciphered text with a given shift.
    Handles both lowercase and uppercase letters.
    Simple and easy-to-understand implementation of the Caesar Cipher.

<h3>Usage</h3>

Clone the repository:

    git clone https://github.com/ami567/PRODIGY_CS_01/caesar-cipher

Navigate to the project directory:

    cd caesar-cipher

To encrypt a message:

    python caesar_cipher.py encrypt "Your message" 3

To decrypt a message:

    python caesar_cipher.py decrypt "Your encrypted message" 3

