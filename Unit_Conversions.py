from math import *
#Meters to inches
def m_t_i(x):
	#39.3701 inches per meter
	y = x * 39.3701
	
	return y
	
#Inches to meters
def i_t_m(x):
	#0.0254 metes per inch
	y = x * 0.0254
	
	return y

#Miles to inches
def mi_t_i(x):
	#63360 inches per mile
	y = x * 63360
	
	return y
	
#Inches to miles
def i_t_mi(x):
	#1.5783E-5 miles per inch
	y = x * (1.5783*(10**(-5)))