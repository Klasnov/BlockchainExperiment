"""
SHA-256 Python Implementation

This is a Python implementation of the SHA-256 cryptographic hash function.
It provides a simple framework for educational purposes, allowing students
to understand the basic structure of the SHA-256 algorithm and experiment
with its behavior.

Author: Kai Lei, Yanming Shao
"""

# The round constants
k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


def right_rotate(x, n):
    """
    Perform bitwise right rotation on a 32-bit integer.

    Args:
        x (int): The 32-bit integer to be rotated.
        n (int): The number of positions to rotate the bits to the right.

    Returns:
            int: The result of the bitwise right rotation.
    """
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF


def sha256(message):
    """
    Compute the SHA-256 hash of the given message.

    Args:
        message (bytes): The input message as a sequence of bytes.

    Returns:
        str: The hexadecimal representation of the computed SHA-256 hash.
    """
    # Initialize hash values (first 32 bits of the fractional parts of the square roots of the first 8 primes)
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # TODO: Your code here
    # Step 1: Pre-processing - Padding the message
    # Step 2: Process the message in 512-bit chunks
    #   - Break the message into 512-bit chunks
    #   - Extend each 16-word chunk to a 64-word chunk
    # Step 3: Initialize working variables to current hash value
    # Step 4: Compression function main loop
    #   - Perform 64 rounds of mixing and transformations
    # Step 5: Add the compressed chunk to the current hash value
    # Step 6: Produce the final hash value

    # Produce the final hash value
    hash_hex = f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}'
    return hash_hex


# Test cases
strings = [
    "Hello, world!",
    "I love blockchain.",
    "This is an experiment with the SHA-256 encryption algorithm."
]

expected_results = [
    "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3",
    "2cf1109d0d2b296e36118f9492135dd6f29980d937d8c97ab781f1d2d8c45a10",
    "e8470d5cb850bab7b46491f5c32508cbb2ce219f1e3dca45066dd9b850c4869a"
]

for index, string in enumerate(strings):
    result = sha256(string.encode()).lower()
    # Print the input string
    print(f"String: {string}")
    # Print the computed hash
    print(f"Computed Hash: {result}")
    # Print the expected hash
    print(f"Expected Hash: {expected_results[index]}")
    # Check if the computed hash matches the expected hash
    print(f"Hashes Match: {result == expected_results[index]}\n")
