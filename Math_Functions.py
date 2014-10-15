# Math Functions for py_calc
# Author: Graeme Bates
# 2013
# This code hopes to demonstrate how a
# calculator actually works behind the scenes

from time import *
from math import *

# Number of loops used in Taylor Series
# (WARNING: LARGE LOOPING MAY CAUSE LARGER ROUNDING ERROR)
number_of_loops = 10

# This function will evaluate a given factorial x: x!
def Factorial(x):
    x = int(x)
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact


def E(x):
    '''(Number) -> float
    Given a number, this function will run the the taylor series for
    e^x.

    >>> E(3)
    20.085536923188

    >>> E(.45)
    1.56831218549
    '''
    # variable y is used to house the answer of our series
    y = 1
    # variable x remains as the original input
    x = (x)
    # variable i acts as our power
    i = 1
    # variable n is used for our for loop
    n = 0

    number_of_loops = 100
    # The loop below is our taylor series (x - ((x^i)/i!) + ((x^i)/i!))
    for n in range(0, number_of_loops):
        # temp is used to store the value for (x^i)/i!
        temp = (((x ** i)/(int(Factorial(i)))))
        # y is then set to y - temp
        y = (y + temp)
        # Here we increment i by one.
        i = i + 1
        # Here we round our answer to the nearest 12 digits
        y = round(y, 12)
        y = float(y)
        # And now we return our answer
        return y


# Sin function for x in radians:
# Sin(x) (function based on the taylor infinite series)
def Sin(x):
    '''(Number) -> float
    Given a number(radians), this function will solve
    the Sine of that number using a function based on
    the Taylor infinite series.

    >>> Sin(.5)
    0.479425538604

    >>> Sin(5.2)
    -0.88345465572
    '''
    # Checking for radian value, if greater than 2 pi,
    # decrease the radian value by factoring out two pi
    if x > (2 * pi):
        rot = x / ((2 * pi))
        rot = int(rot)
        x = x - (2 * pi * rot)
        # variable y is used to house the answer of our series
        y = (x)
        # variable x remains as the original input
        x = (x)
        # variable i acts as our power
        i = 3
        # variable n is used for our for loop
        n = 0

        # The loop below is our taylor series (x - ((x^i)/i!) + ((x^i)/i!))
        for n in range(0, number_of_loops):
            # temp is used to store the value for (x^i)/i!
            temp = (((x ** i) / (int(Factorial(i)))))
            # y is then set to y - temp
            y = (y - temp)
            # Here we increment i by two.
	    # (sin as an odd fucntion, i is always an odd number)
            i = i + 2
            # similarly to above, temp is used to store (x^i)/i!
            # but is set negative since the series alternated
            # between plus and minus
            temp = (-1 * ((x ** i) / (int(Factorial(i)))))
            y = (y - temp)
            # Again we increment i by two
            i = i + 2
        # Here we round our answer to the nearest 12 digits
        y = round(y, 12)
        y = float(y)
        # And now we return our answer
        return y


# Cos function for x in radians: Cos(x)
def Cos(x):
    '''(Number) -> float
    Given a number(radians), this function will solve
    the Cosine of that number using a function based
    on the Taylor infinite series.

    >>> Cos(.5)
    0.87758256189

    >>> Cos(19.5)
    0.795814969814
    '''
    # Cos function uses the same variables and
    # radian check as our sin function above.
    if x > (2*pi):
        rot = x / ((2 * pi))
        rot = int(rot)
        x = x - (2 * pi * rot)
        y = 1
        x = (x)
        i = 2
        n = 0

    # This loop is very similar to our Sin taylor series but
    # is in the form (1 - ((x^i)/i!) + ((x^i)/i!)) where i is
    # always an even number (i.e. cos is an even funciton)
    for n in range(0, number_of_loops):

        temp = (((x ** i) / (int(Factorial(i)))))
        y = (y - temp)
        i = i + 2
        temp = (-1 * ((x ** i) / (int(Factorial(i)))))
        y = (y - temp)
        i = i + 2
        y = round(y, 12)
        y = float(y)
        return y


# Tan function for x in radians: Tan(x)
def Tan(x):
    '''(Number) -> float
    Given a number(radians), this function will output the Tangent,
    using the Sine and Cosine function we defined above.

    >>> Tan(4)
    1.157821282349

    >>> Tan(2.368)
    -0.976663396733
    '''
    # Tan function is Sin(x)/Cos(x)
    # Here we get our values for Sin(x) and Cos(x) and set them to
    # s and c respectively
    s = Sin(x)
    c = Cos(x)

    s = (s)
    c = (c)
    # Tan = y = s/c = Sin(x)/Cos(x)
    y = s / c

    y = round(y, 12)

    return y


# Csc function for x in radians: Csc(x)
def Csc(x):
    '''(Number) -> float
    Given a number in radians this funtion will output the Cosecant

    >>> Csc(3)
    7.086167395730519
    '''
    # The Csc function is the inverse of the Sin function (i.e. 1/Sin(x))
    y = 1 / (Sin(x))
    return y


# Sec function for x in radians: Sec(x)
def Sec(x):
    '''(Number) -> float
    Given a number in radians this funtion will output the Secant

    >>> Sec(1)
    1.8508157176814042
    '''
    # The Sec function is the inverse of the Cos function (i.e. 1/Cos(x))
    y = 1 / (Cos(x))

    return y


# Cot function for x in radians: Cot(x)
def Cot(x):
    '''(Number) -> float
    Given a number in radians this funtion will output the Cotangent

    >>> Cot(9)
    -2.2108454109982656
    '''
    # The Cot function is the inverse of the Tan function (i.e. 1/Tan(x))
    y = 1 / (Tan(x))

    return y

# Square root for x: Root(x)
def Root(x):
  '''(Number) -> float
  Given a number, this function will output the an esimated root

  >>> Root(6)
  2.44948974278
  '''
  # Here we are going to use the Babylonian Method
  # The Babylonian method uses guesses to estimate the square root like so:
  # sqr(6) Guess 2. 6/2 = 3. 2+3/2 = 2.5. 6/2.5 = 2.4. 2.4+2.5/2 = 2.45
  # 6/2.45 = 2.4489... As you can see we start getting closer and close to the
  # real solution (2.44948...) very quickly.
  y = float(2)
  for n in range (0, 10):
    temp_val = (x / y)
    y = ((y + temp_val) / 2)
  y = round(y, 12)
  return y
