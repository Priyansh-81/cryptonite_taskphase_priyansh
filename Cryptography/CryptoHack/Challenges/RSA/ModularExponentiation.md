# **Modular Exponentiation**

## Solution:
For this challenge we just need to solve the modular exponentiaiton problem ```10117mod22663```, pretty simply, i just used the built in python function to get the solution to the expression 

### Code:
```
pow(101,17,22663)

```
### Note: 
Modular exponentiation is the remainder when some integer a is raised to some power m lets say, and then devided by some positive integer n.

so basically 
r= a^m mod n

here mathematically 

a=101
m=17
and 
n= 22663


So after feeding this in pow built in operation in python,i got the flag...
(used idle)

#### ```flag: 19906```

![image](images/Screenshot%202025-01-03%20at%201.35.40 AM.png)