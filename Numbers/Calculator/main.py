# Calculator - A simple calculator to do basic operators. Make it a scientific
# calculator for added complexity.


# Used to check if a valid number was entered
def isfloat(num):
	try:
		# Checks for 'NaN' because float() will not count this as an invalid
		# number.
		if num == 'NaN':
			print('Please enter a valid number')
			return 'fail'

		# If the number is valid, returns the number after being converted to a
		# float.
		float(num)
		return (float(num))

	# If the number was invalid, returns 'fail'
	except ValueError:
		print('Please enter a valid number')
		return 'fail'

# Calculates an operation on the two given numbers
def calc(first, second):
	while True:
		operation = input('Please enter an operation you would like to perform' +
		'on the two numbers (+,-,*,/): ')

		# Performs the given calculation and returns the result
		if operation == '+':
			return first + second
		elif operation == '-':
			return first - second
		elif operation == '*':
			return first * second
		elif operation == '/':
			return first / second
		
		# Will continue to loop until the user enters a valid operation
		else:
			print('Please enter a valid operation')


def main():
	# Loops for the first and second number entry until the user a valid number

	while True:
		first = input('Please enter the first number (negative and decimal ' +
		'numbers work): ')

		if isfloat(first) != 'fail':
			break

	while True:
		second = input('Please enter the second number (negative and decimal' +
		' numbers work): ') 

		if isfloat(second) != 'fail':
			break

	# Prints out the resulting calculation
	print('The resulting calculation is:', calc(float(first), float(second)))


if __name__ == '__main__':
	main()
