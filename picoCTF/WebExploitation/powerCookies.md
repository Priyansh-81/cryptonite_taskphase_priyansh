# **Power Cookies**

## Problem:
![question](images/powercookiesq.png)

## Solution:
On visiting the link, we had a button saying continue as guest, but click that did not say anything...now as the title suggest we have to tamper with the cookies in order to get flag, we have to give access to everyone.
![image](images/powercookies1.png)
Now that what i did, by changing the value of isAdmin to 1, then i did refresh, but it did not work the same.
![image](images/powercookies2.png)

So i tried the same using a different browser as i was confident about what i am doing, (because of previous OASIS CTF experience), so thats what i tried with chromium.

And i got the flag.
![images](images/powercookies3.png)

### flag: ```picoCTF{gr4d3_A_c00k13_65fd1e1a}```