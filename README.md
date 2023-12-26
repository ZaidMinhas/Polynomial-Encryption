# Polynomial-Encryption
This is an encryption algorithm that to encrypt any ascii text

## Function
Program has a function f(x) that encrypts text
f(x) if a polynomial function that has the form f(x) -> $a*(b*x + c)^d$
g(x) is the inverse function of f(x) that returns the decrypted/original text
default a,b,c,d values are set in the code but can be changed

## Basic Usage
```py
import PolyCryption as PC

x = PC.Encrypt(text)
y = PC.Decrypt(x)
```

## To change coefficents
```py
PC(2,4,5,3)
# a,b,c,d = 2,4,5,3

#or
PC.a = 23
# only a is changed
```

## Caution 

Although the encryption algorithm works fine, using large coefficents for 'd' will result in large encrypted numbers, therefore I recommend using smaller values for d. To be more technical you could say the length of each encrypted character is `O(a*(b*n + c)^d)`

0 can only be used for c
and to just get the ascii of each letter set to `P(1,1,0,1)`

Negative numbers can be used for some of the values, however I heavily discourage using it
