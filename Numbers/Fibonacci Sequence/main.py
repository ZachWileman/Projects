# Fibonacci Sequence - Enter a number and have the program generate the
# Fibonacci sequence to that number or to the Nth number.

# Program developed using Python 3.4.4

#Used for determining fibonacci
def getFib (fib, prevNum, nextNum, sequence):
	
	# Used for exiting the recursive function
	if fib == sequence:
		return

	# Used for the first fibonacci number
	if sequence == -1:
		print("0", end=" ")
		getFib(fib, 0, 1, sequence+1)

	# Used for the second fibonacci number
	elif sequence == 0:
		print("1", end=" ")
		getFib(fib, 0, 1, sequence+1)

	# Used for all fibonacci numbers after the second number
	else:
		prevNum, nextNum = nextNum, (prevNum+nextNum)
		print(nextNum, end=" ")
		getFib(fib, prevNum, nextNum, sequence+1)

# Iterates until the user enter a correct number
while True:
	fib = input("""\
Please enter an integer that you would like to generate Fibonacci to
(your number > -1): """)
	
	fib = int(fib)
	
	if fib > -1:
		break
	else:
		print("\nInvalid number entered!\n")

# Recursively generates the fibonacci sequence to the nth integer
getFib(fib, 0, 1, -1)
