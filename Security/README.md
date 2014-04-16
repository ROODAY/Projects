Security
-------------

**Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.

**Password Protected Data (FINISHED)** - The passwordprompt.py file has the code. What it does is it stores a password, (later will be called from a file), asks for input, compares input to password, then if correct gives option to read data or write to data. Writing is caesar shifted randomly between 3-5 units in ASCII. The random shift is saved as first unit in string, so when decoding, first unit in string is used as guide for reversing the shift, and the unit is deleted from the print to keep it clean.  *Special Thanks to Noah Huppert for supplying the very elegant offset() method!*
