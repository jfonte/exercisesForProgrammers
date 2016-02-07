# simple program that prompts for name and prints a greeting absed on it.

#!/usr/bin/python

import time

# print(time.strftime("%H"))

time_of_day = 'evening'
if int(time.strftime("%H"))<12:
 	time_of_day = 'morning'
 
# print(time_of_day)
print('> Good ' +time_of_day +' stranger.')
# name = 'josh'
name = input('> What shall I call you? ')
if name =='Falken':
	print("> Professor Falken! It has been a longtime! Glad you are back!")
else:
	print('> Nice to meet you', name)