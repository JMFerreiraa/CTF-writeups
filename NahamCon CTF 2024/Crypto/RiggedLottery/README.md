# **Rigged Lottery**
#*Challenge Author: @awesome10billion*

The solution to this challenge was on a paper that is linked to this code on github:
https://github.com/prowlett/lottery-guaranteed-win

This code was built to handle ball values between 1 and 60 while our challenge goes to 70.

While there are more optimized methods, an easy solution is to copy the conclusions from the paper, including the vector they reached, and add all possible combinations for the last 10 elements with values between 1 and 8. This approach is based on the fact that the paper created 5 clusters, so we just need to assign the missing values to one of these clusters. (Reading the paper for a thorough understanding is advised!)

Solution provided on ```solve.py```
