# **SQL Direct**

## Problem:
![question](images/sqldq.png)
For this challenge, we have to connect to PostgreSQL server, to get the flag.

## Solution:

### Port: ```psql -h saturn.picoctf.net -p 65004 -U postgres pico```

First of all, I did not know what exactly is PostgreSQL, so after googling for a bit, i got to know its just a RDBMS system, so u tried conncecting to the server using the given command...
Then i realised its not preinstalled in my os, so i used Homebrew to install the software 
![image](images/sqld1.png)
After which I listed all the commands using the ```help``` commad, then ```\?``` and ```\h``` tags, then using the ```\l``` tag, i listed all the availble databases, then using ```\dt``` i listed all the tables in the pico database, then i tried to list the contents of the flags table, but i was making mistake with indexing or something ig, after trying for a while i finnally got the flag.

![image](images/sqld2.png)

![image](images/sqld3.png)

![image](images/sqld4.png)

![image](images/sqld5.png)

### flag: ```picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}```