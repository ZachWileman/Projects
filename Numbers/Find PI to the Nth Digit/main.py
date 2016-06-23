#Find PI to the Nth Digit - Enter a number and have the program generate PI up
#to that many decimal places. Keep a limit to how far the program will go.

import math

keepGoing = True

while keepGoing:
	while True:
	    decimalPlace = input("""\
	   	Please enter a decimal place that you would like to round PI up to:
	    (0 < your number < 15)
	    """)

	    decimalPlace = int(decimalPlace)

	    if decimalPlace <= 0 or decimalPlace > 15:
	        print("The number you entered was invalid, please try again.")
	    else:
	    	break

	x = round(math.pi, decimalPlace)
	print(x)

	keepAsking = True

	while keepAsking:
		repeat = input("""\
		Would you like to enter another decimal place to round PI up to?
		(y = yes, n = no)
		""")
	        
		if repeat == 'n':
		    keepGoing = False
		    break
		elif repeat != 'y':
			print("Sorry, what was that?")
		else:
			keepAsking = False
