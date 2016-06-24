# Alarm Clock - A simple clock where it plays a sound after X number of
# minutes/seconds or at a particular time.

import time
import winsound

while True:
    choice = input('Would you like to use the timer or alarm clock? ' +
    '(a = alarm clock, t = timer)')

    if choice == 't':
        tmr = float(input('\nPlease enter the time for the timer in seconds ' +
        ' Ex.(43): '))
        
        time.sleep(tmr)
        winsound.PlaySound('ship_bell.wav', winsound.SND_FILENAME)
        break

    elif choice == 'a':
        tm = time.strftime('%I:%M %p', time.localtime())
        print ('\nThe current time is', tm)
        
        alarmClock = float(input('Please enter at what time you would like ' +
        'the alarm to chime. Ex.(): '))

        
        break

    else:
        print('Please enter a valid choice.')
