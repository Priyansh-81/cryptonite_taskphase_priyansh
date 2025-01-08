# **Public Keys**

## Solution:

For this challenge, we just have to encrypt the message here 12, with RSA , the exponents and modulus are given as key, so straight forward using the pow operation, i got the encrypted message which is the flag

exponent= 65537(in general)
modulus= 17*23

### Code:
```
pow(12,65537,17*23)
```
#### flag: ```301```

![image](images/Screenshot%202025-01-03%20at%202.04.43 AM.png)