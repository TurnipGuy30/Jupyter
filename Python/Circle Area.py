'''
Calculate the area of a circle with the radius as input
'''

### Change these:
decimalPlaces = 5
###

import math

def circle_area(radius):
	return f'Area of circle: {round(math.pi * math.pow(float(radius), 2), decimalPlaces)} units^2 ({decimalPlaces}dp)'

try:
	print(circle_area(input('Radius of circle: ')))
except:
	print('Please provide a number!')
	
input('Press Enter to exit.')
