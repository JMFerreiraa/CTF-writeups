# **Magic RSA**
#*Challenge Author: @Jstith*

RSA is only secure because the values of "e" and "p" are very high.

On this challenge we had access to the value of "e" being 3.

The value of "e" is so low that the modulus will have no inpact of the encrypted value. For example mod(10, 99999) = 10.

So we can just perform a simple operation to get the flag as described on ```solve.py```