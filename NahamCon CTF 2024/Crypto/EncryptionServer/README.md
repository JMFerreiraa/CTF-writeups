# **Encryption Server**
#*Challenge Author: @Jstith*

RSA is only secure because the values of "e" and "p" are very high.

On this challenge we had access to the value of "e" being between "500" and "1000".

After connecting to the challenge, we could print the encrypted flag and the N (modulus) it was used to encrypt it.

Knowing that the value of "e" was between 500 and 1000, and knowing the first encrypted char was "f" from "flag", we could bruteforce all possible values of e until we got the correct value of "e" that was used.

Finally, with the value of "N" and "e", we can now encrypt any value. This way we could encrypt all possible chars and see which one matches the encrypted values of the flag, just like a rainbow table :D!

Solution described on ```solve.py```