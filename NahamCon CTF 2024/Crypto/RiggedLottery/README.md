# **Rigged Lottery**
#*Challenge Author: @awesome10billion*

The solution to this challenge was on a paper that is linked to this code on github:
https://github.com/prowlett/lottery-guaranteed-win

This code was built to handle ball values between 1 and 60 while our challenge goes to 70.

There are more optimized ways of doing this but a possible easy solution was to copy the paper conclusions, the vector they reached and add all possible combinations for the last 10 withe the values between 1 and 8. (The reason for this is that on the paper they have created 5 clusters, so we just need to add the missing values to one of the clusters. Reading the paper is advised!)

Solution provided on ```solve.py```