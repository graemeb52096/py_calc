from math import *
#Meters to inches
def m_t_i(x):
	'''(number) -> float
	Given a number(meters), this function will out put the equivelent
	in inches
	
	>>> m_t_i(2)
	78.7402
	
	'''
	#39.3701 inches per meter
	y = x * 39.3701
	
	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)
	
	return y
	
#Inches to meters
def i_t_m(x):
	'''(number) -> float
	Given a number(inches), this function will out put the equivelent
	in meters
	
	>>> i_t_m(12)
	0.3048
		
	'''	
	#0.0254 metes per inch
	y = x * 0.0254

	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)	
	
	return y

#Miles to inches
def mi_t_i(x):
	'''(number) -> float
	Given a number(miles), this function will out put the equivelent
	in inches
		
	>>> mi_t_i(2)
	126720
		
	'''	
	#63360 inches per mile
	y = x * 63360
	
	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)	
	return y
	
#Inches to miles
def i_t_mi(x):
	'''(number) -> float
	Given a number(inches), this function will out put the equivelent
	in miles
		
	>>> i_t_mi(78)
	0.001231074
	
	'''	
	#1.5783E-5 miles per inch
	y = x * (1.5783*(10**(-5)))
	
	#Here we round our answer to the nearest 12 digits	
	y = round(y, 12)	
	return y	