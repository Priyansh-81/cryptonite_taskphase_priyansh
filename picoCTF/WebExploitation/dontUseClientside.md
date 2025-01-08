# **dont-use-client-side**

## Problem:
For this challenge, we are given a link to web page for student portal, from there we need the flag.

![question](images/dclientq.png)

## Solution:
For this challenge, i first tried some random requests, but nothing happended, after which I opened the web inspector, went over the source code, saw some java script function containing ```pico``` and ```CTF{``` substring, after going through the snipped i realised, its just the password string splitted into sub string so manually i just merged them all and i got the flag.

![image](images/dclientans.png)

### flag: ```picoCTF{no_clients_plz_7723ce}```