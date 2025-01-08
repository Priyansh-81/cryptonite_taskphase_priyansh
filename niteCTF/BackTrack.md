# **Back Track**

## Problem:

Kenji is a nice guy who lives in Tokyo. He is in a dilemma. In 2017, he was late to an important meeting and is now facing repercussions. To defend himself, he needs to prove that it was not his fault. His evidence? The train he boarded that day, traveling between Omotesando and Suitengumae, was delayed. However, his boss is not providing the specific details of the accusation. Kenji vividly remembers one key fact: the train was around 61 minutes late.

Help him uncover the exact date of the incident and the start time of the delay. Justice for Kenji!

Flag Format: nite{time_date}

Example: nite{13:00_3January}

*_For this challenge we are supposed to gather the train timings and the date, between Omotesando and Suitengumae._*

## Solution:

So, first I checked what metro line was this train running on, after googling, I found that, this train runs on **Hanzomon** metro line, so i checked the train delay status for that specific line on the website ```https://www.tokyometro.jp/lang_en/delay/history/hanzomon.html```, this gave me the train status for, current time...Now for checking 2017 status, I used the web archive tool called **WAYBACK Machine**, URL: ```web.archive.org```, In there I added the URL for the delay website, which loaded the page from 2017, after which i just clicked on the march 26th archive snapshot in 2017 section, there i checked trains with delay of 61mins, there i got the train details, the train was on 20th February departing at 5 pm.

![images](images/Screenshot%202024-12-13%20at%208.56.47 PM.png)
![images](images/Screenshot%202024-12-13%20at%208.56.24 PM.png)


So the flag was 

### flag: ```nite{17:00_20February}```