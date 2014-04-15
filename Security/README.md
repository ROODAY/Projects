Security
-------------

**Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.

**Passworded Protected Data** - Made a system that prompts for a password, then when given the password reads a file of encyrpted data, decrypts, and then shows the data. (Optional: Add in ability to encrypt data and append to file)