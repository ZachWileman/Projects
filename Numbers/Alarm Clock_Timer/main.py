# Alarm Clock/Timer - A simple clock where it plays a sound after X number of
# minutes/seconds or at a particular time.

# Program developed using Python 3.4.4

import time
import re
import winsound

while True:

    # Asks user for timer or alarm clock
    choice = input('Would you like to use the timer or alarm clock? ' +
    '(a = alarm clock, t = timer): ')

    # Timer
    if choice == 't':

        while True:
            # Gets user input for timer as well as validates the user's input
            try:
                tmr = int(input('\nPlease enter the time for the timer in ' +
                'seconds. Ex:(15) NOTE: Needs to be an integer:  '))

            # If the user doesn't enter an integer
            except ValueError:
                print('Please enter a valid number.')

            else:
                # If the value is below 0
                if tmr < 0:
                    print('Please enter a valid number.')
                
                # Otherwise, breaks from the loop since the input is valid
                else:
                    break
        
        # Waits user specified amount of time, then alarm sounds
        while tmr:
            print(tmr, end=' \r')
            time.sleep(1)
            tmr -= 1

        print(tmr, end=' \r') # Used to print out the 0 seconds left
        winsound.PlaySound('wuba.wav', winsound.SND_FILENAME)
        
        break # Exits the program

    # Alarm clock
    elif choice == 'a':
        timeFormat = ('^\d{2}:\d{2}\s[A|P]M') # Used for validating user input

        # Prints out the current time
        tm = time.strftime('%I:%M %p', time.localtime())
        print ('\nThe current time is', tm)
        
        while True:
            # Gets user input for alarm clock time
            alarmClock = input('Please enter at what time you would like the' +
            ' alarm to chime. \nEx:(10:10 PM) NOTE: There is a space between' +
            ' the \'10:10\' and \'PM\': ')

            # Validates user input
            if re.fullmatch(timeFormat, alarmClock):
                break
            else:
                print('\nPlease enter a valid time format.')

        # Loops until the current time matches the user inputted time
        while True:
            if alarmClock == time.strftime('%I:%M %p', time.localtime()):
                winsound.PlaySound('wuba.wav', winsound.SND_FILENAME)
                break # Breaks from the alarm clock check
        
        break # Exits the program

    # Invalid input
    else:
        print('Please enter a valid choice.\n')
