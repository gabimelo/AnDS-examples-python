"""
@author Gabriela Melo
@since 23/03/15
@modified 27/03/15
"""

# |m|
# @param: m, integer from which absolute value is going to be returned
# @pre: none 
# @post: prints absolute value of m
# @complexity: best and worst case are the same: O(1)
		.data

		.text

		addi	$v0, $0, 5  	# $v0 = int(input())
		syscall 		   

   		bgt 	$v0, $0, pos  	# if positive, go to pos
   		neg 	$a0, $v0 		# $a0 = - $v0
   		j 		exit

pos: 	move    $a0, $v0 		# $a0 = $v0

exit: 	addi 	$v0, $0, 1
		syscall 				# prints $a0

		addi	$v0, $0, 10		# exit
		syscall

# pythagorian
# @param: m and n, two numbers from which the pythagorian triple is going to be generated
# @pre: none 
# @post: prints pythagorian triple constructed from user's inputs
# @complexity: best and worst case are the same: O(1)

				.data
prompt:	.asciiz "Enter two numbers: "
m:		.word 	0
n: 		.word 	0
a:		.word 	0
b:		.word 	0
c:		.word 	0
obrack: 	.asciiz "( "
cbrack: 	.asciiz ")"
comma: 	.asciiz	", "

		.text

		la 		$a0, prompt 	 # print("Enter two numbers: ")
		addi 	$v0, $0, 4
		syscall		

		addi	$v0, $0, 5		# m = int(input())
		syscall
		sw		$v0, m

		addi	$v0, $0, 5		# n = int(input())
		syscall
		sw		$v0, n

		lw 		$t0, m
		mult 	$t0, $t0
		mflo 	$t0 			# $t0 = m**2

		lw 		$t1, n
		mult 	$t1, $t1
		mflo 	$t1 			# $t1 = n**2

		add 	$t2, $t0, $t1 	# $t2 = m**2 + n**2
		sw 		$t2, c 			# c = m**2 + n**2

		sub 	$t2, $t0, $t1 	# $t2 = m**2 - n**2

		bgt 	$t2, $0, pos  	# if positive, go to pos
   		neg 	$t2, $t2 		# $t2 = - $t2

pos:	sw	$t2, a

		lw 	$t0, m
		lw	$t1, n
		mult	$t0, $t1
		mflo 	$t0      	# $t0 = m * n
		addi 	$t1, $0, 2
		mult	$t0, $t1
		mflo 	$t0			# $t0 = 2 * m * n	
		sw	 	$t0, b

		la 		$a0, obrack # print("( ")
		addi 	$v0, $0, 4
		syscall	

		lw 		$a0, a  	# print("a")
		addi 	$v0, $0, 1
		syscall	

		la 		$a0, comma  # print(", ")
		addi 	$v0, $0, 4
		syscall	

		lw 		$a0, b  	# print("b")
		addi 	$v0, $0, 1
		syscall	

		la 		$a0, comma  # print(", ")
		addi 	$v0, $0, 4
		syscall	

		lw 		$a0, c  	# print("c")
		addi 	$v0, $0, 1
		syscall	

		la 		$a0, cbrack # print(")")
		addi 	$v0, $0, 4
		syscall

		addi	$v0, $0, 10	# exit
		syscall

# isLeapYear.asm
# @param: year to be tested for leap year
# @pre: year >= 1582 
# @post: prints "Is a leap year" if inputed item is a leap year
#  	     if not, prints "Is not a leap year"
# @complexity: best and worst case are the same: O(1)
		.data
prompt:	.asciiz "Enter a year (greater than 1582): "
year: 	.word 	0
leap: 	.word 	0   	#leap = False
is:		.asciiz "Is a leap year"
isnt:	.asciiz "Is not a leap year"

		.text

		la 		$a0, prompt  	# print("Enter a year (greater than 1582):  ")
		addi 	$v0, $0, 4
		syscall	

		addi	$v0, $0, 5		# year = int(input())
		syscall
		sw		$v0, year

		lw		$t0, year 		# $t0 = year
		rem 	$t1, $t0, 4 	# $t1 = $t0 % 4
		bne 	$t1, $0, case2
		
		rem 	$t1, $t0, 100 	# $t1 = $t0 % 100
		beq		$t1, $0, case2
		
		addi 	$t2, $0, 1 		# $t2 = 1
		sw		$t2, leap 		# leap = 1
		j 		true

case2:  lw		$t0, year 		# $t0 = year
		rem 	$t1, $t0, 400 	# $t1 = $t0 % 400
		bne 	$t1, $0, false

		addi 	$t2, $0, 1 		# $t2 = 1
		sw		$t2, leap 		# leap = 1
		j 		true

false:  la 		$a0, isnt 		# print("Is not a leap year")
		addi 	$v0, $0, 4
		syscall	
		j 		exit

true:   la 		$a0, is  		# print("Is a leap year")
		addi 	$v0, $0, 4
		syscall	

exit: 	addi	$v0, $0, 10		# exit
		syscall

# Task 3
# @param: size of list and list items
# @pre: 
# @post: sums list items up to first negative number
# @complexity: best and worst case are the same: O(n)
		.data
prompt1: .asciiz "Enter size of list: "
prompt2: .asciiz "Enter next item in the list: "
i: 		.word	0
sum:	.word 	0
size: 	.word 	0
the_list: .word 	0

		.text

		la 		$a0, prompt1  	# print("Enter size of list: ")
		addi 	$v0, $0, 4
		syscall

		addi	$v0, $0, 5		# size = int(input())
		syscall
		sw		$v0, size

		lw		$t0, size 		# $t0 = size	
		
reading: 	lw 		$s0, i
		beq 	$t0, $s0, begin
		
		la 		$a0, prompt2  	# print("Enter next item in the list: ")
		addi 	$v0, $0, 4
		syscall

		addi	$v0, $0, 5		# mem[the_list+4+i*4]= int(input())
		syscall
		mul 	$t2, $s0, 4 	# $t2 = i * 4
		sw		$v0, the_list($t2)
		addi	$s0, $s0, 1
		sw 	$s0, i
		j 		reading


begin:	sw 		$0, i 

while:		lw 		$s0, i
		beq 	$t0, $s0, exit 	# if i == size: jump to exit
		mul 	$t3, $s0, 4 	# $t3 = i * 4 
		lw 	$t4,the_list($t3) 
		bgt 	$0, $t4, exit   # if item is negative, exits

		lw 		$t1, sum 		# $t1 = sum
		add 	$t1, $t1, $t4 	# $t1 = sum + list[i]
		sw 		$t1, sum		# sum = $t1
		
		addi	$s0, $s0, 1
		sw 	$s0, i
		
		j 		while

exit:   lw 		$a0, sum  		# print(sum)
		addi 	$v0, $0, 1
		syscall	
		addi	$v0, $0, 10		# exit
		syscall