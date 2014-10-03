#import required libraries
from decimal import *
from time import *
from math import *
from threader import *

#Number of loops used in Taylor Series (WARNING: LARGE LOOPING MAY CAUSE LARGER ROUNDING ERROR)
number_of_loops = 10

#Function change print color
def print_color(this_color, string):
    return "\033[" + this_color + "m" + string + "\033[0m"

#Color value is set to a purple like color but can be changed by editing value below
color_val = str(35)

#This function will evaluate a given factorial x: x!
def Factorial(x):
	x = int(x)
	fact=1
	for i in range(1,x+1):
		fact=fact*i
	return fact
	
def E(x):
	#variable y is used to house the answer of our series
	y = 1
	#variable x remains as the original input
	x = Decimal(x)
	#variable i acts as our power
	i = 1
	#variable n is used for our for loop
	n = 0
	
	number_of_loops = 200
    
	
	#The loop below is our taylor series (x - ((x^i)/i!) + ((x^i)/i!)) 
	for n in range (0, number_of_loops):
		
		#temp is used to store the value for (x^i)/i!
		temp = Decimal(((x**i)/(int(Factorial(i)))))
		#y is then set to y - temp
		y = Decimal(y + temp)
		
		#Here we increment i by one.
		i = i + 1
	
	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)
		
	number_of_loops = 10
	#And now we return our answer	
	return y

#Sin function for x in radians: Sin(x) (function based on the taylor infinite series)
def Sin(x):
	#Checking for radian value, if greater than 2 pi, decrease the radian value by factoring out two pi
	if x > (2*pi):
		rot = x/(Decimal(2*pi))
		rot = int(rot)
		x = x - Decimal(2*pi*rot)
	#variable y is used to house the answer of our series
	y = Decimal(x)
	#variable x remains as the original input
	x = Decimal(x)
	#variable i acts as our power
	i = 3
	#variable n is used for our for loop
	n = 0
	
	#The loop below is our taylor series (x - ((x^i)/i!) + ((x^i)/i!)) 
	for n in range (0, number_of_loops):
		
		#temp is used to store the value for (x^i)/i!
		temp = Decimal(((x**i)/(int(Factorial(i)))))
		#y is then set to y - temp
		y = Decimal(y - temp)
		
		#Here we increment i by two. (sin as an odd fucntion, i is always an odd number)
		i = i + 2
		
		#similarly to above, temp is used to store (x^i)/i! but is set negative since the series alternated between plus and minus
		temp = Decimal(-1 * ((x**i)/(int(Factorial(i)))))
		y = Decimal(y - temp)
		
		#Again we increment i by two
		i = i + 2
	
	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)
		
	#And now we return our answer	
	return y

#Cos function for x in radians: Cos(x)
def Cos(x):
	#Cos function uses the same variables and radian check as our sin function above.
	if x > (2*pi):
		rot = x/(Decimal(2*pi))
		rot = int(rot)
		x = x - Decimal(2*pi*rot)
	y = 1
	x = Decimal(x)
	i = 2
	n = 0
	
	#This loop is very similar to our Sin taylor series but is in the form (1 - ((x^i)/i!) + ((x^i)/i!)) 
	#where i is always an even number (i.e. cos is an even funciton)
	for n in range (0, number_of_loops):


		temp = Decimal(((x**i)/(int(Factorial(i)))))
		y = Decimal(y - temp)
		
		i = i + 2
		
		
		temp = Decimal(-1 * ((x**i)/(int(Factorial(i)))))
		y = Decimal(y - temp)
		
		i = i + 2
	
	
	y = round(y, 12)
	
	return y

#Tan function for x in radians: Tan(x)	
def Tan(x):
	#Tan function is Sin(x)/Cos(x)
	#Here we get our values for Sin(x) and Cos(x) and set them to s and c respectively 
	s = Sin(x)
	c = Cos(x)
	
	s = Decimal(s)
	c = Decimal(c)
	
	y = s/c
	
	y = round(y, 12)
	
	return y

#Csc function for x in radians: Csc(x)	
def Csc(x):
	#The Csc function is the inverse of the Sin function (i.e. 1/Sin(x))
	y = 1/(Sin(x))
	
	return y

#Sec function for x in radians: Sec(x)
def Sec(x):
	#The Sec function is the inverse of the Cos function (i.e. 1/Cos(x))
	y = 1/(Cos(x))
	
	return y	

#Cot function for x in radians: Cot(x)	
def Cot(x):
	#The Cot function is the inverse of the Tan function (i.e. 1/Tan(x))
	y = 1/(Tan(x))
	
	return y
	

