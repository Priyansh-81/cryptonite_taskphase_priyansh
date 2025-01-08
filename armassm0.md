# **ARMssembly 0**

## Problem:

Just feed the values as arguments to the code given, and give the answer wrapped in a certain format. That is a flag.

## Solution:
```
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi                                convert string to int
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi                                convert string to int
	mov	w1, w0                              
	mov	w0, w19
	bl	func1                               calling func1 function
	mov	w1, w0                              store result in w1
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf                              calling printf function
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
```

```
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0                              comparing these 
	bls	.L2                                 if w1<=w0, then move to label L2
	ldr	w0, [sp, 12]                        else return larger value
	b	.L3
```

so basically flag is the larger value

picoCTF{F66B01EC}