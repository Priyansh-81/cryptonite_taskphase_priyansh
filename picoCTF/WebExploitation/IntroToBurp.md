# **Intro to Burp**

## Problem:
Here we have to get the flag from a given link...
![question](images/burpq.png)

## Approach:
As the name suggests, we have to use a tool called burp, so after reseaching about burp, i got to know about the tool called burpsuite which is used to instersept requests. Initially i was not sure what we were supposed to do about the 2fa page, after reading the hint, i got to know we have mingle with the POST request..


First I opened the link in the burpsuite browser to get the requests as required, then after checking the requests in the Proxy tab(after setting it as a repeater), I removed the 2fqa request entirely , which gave me the flag...

![image](images/burp1.png)
![image](images/burp2.png)
![image](images/burp3.png)
![image](images/burp4.png)
![image](images/burp5.png)
![image](images/burp6.png)
![image](images/burp7.png)
![image](images/burp8.png)
![image](images/burp9.png)

### flag: ```picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}```
