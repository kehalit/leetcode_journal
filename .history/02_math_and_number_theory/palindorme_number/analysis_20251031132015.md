what is palindrome ?
-- an integer when it reversed it remains the same
for example 12321 is palindrome 

Initial Edge Cases 
- negative number can not be palindromes so x is positive integer 
- if number ends with 0 i reverse must start with zeron so can not be palindrome
    120 !== 021 which is 21

Variables Initialization

- let reverse = 0: Initializes a variable to build the reversed version of x.
- let n = x: Creates a temporary copy of the input number x  to manipulate within the loop. This is crucial because we need to preserve the original value of x for the final comparison.

Algorithm Steps
Step 1 — Reverse the Number

-  extract each digit from the end of n using the modulus operator (%) and rebuild the reversed number by multiplying the current reverse by 10 and adding that digit.