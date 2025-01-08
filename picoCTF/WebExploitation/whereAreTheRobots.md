# **Where are the robots**

## Problem:
![question](images/robotsq.png)

## Solution:
For this challenge, first i check ever aspect of the website in the inspector and saw nothing, after which i checked the hint, again after which also i had no clue, how to do the challenge, so after doing some google search I got to know about how someone can avoid certain keywords or something being stored in the search index of a certain browser...(source: ```https://www.youtube.com/watch?v=QMzeiTov6a8```), so I went to the robots.txt file of the webpage using the link ```https://jupiter.challenges.picoctf.org/problem/56830/robots.txt```

![robot.txt](images/robots1.png)

There i saw the Disallowed webpage, so i went to the particular htmp page by changing the URL.

```https://jupiter.challenges.picoctf.org/problem/56830/1bb4c.html```, then i got the flag.

![htmlpage](images/robots2.png)

### flag: ```picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}```
