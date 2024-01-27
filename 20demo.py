# 20demo.py by Amina Muhic

import math
import sys

print('hello, again')           # greeting
def greeting():                 # greeting as a function
	print('hello yourself')
greeting()
s = 'hello world'               # string
print(s, type(s))

# math
print(1.5e-2)                   # numbers
print(2 + 2)                    # + addition
print(10 - 5)                   # - subtraction
print(6 * 6)                    # * multiplication
print(44 / 3)                   # / division
print(2 ** 0)                   # ** exponentiation
print(4 // 3)                   # // integer divide
print(4 % 3)                    # % remainder
print(10 / (5 - 3))             # () precedence

# math functions
print(abs(-2))                  # absolute value
print(pow(3, 2))                # e.g., 3 to the power of 2
print(round(math.e, ndigits=3)) # round off e to 3 digits
print(math.ceil(5.897))         # round up
print(math.floor(5.879))        # round down
print(math.log(math.e))         # log base e
print(math.log2(2))             # log base 2
print(math.log10(10))           # log base 10
print(math.sqrt(64))            # square root
print(math.pow(3, 2))           # e.g., 3 to the power of 2
print(math.factorial(4))        # factorial of integer

# variables
a = 3                           # side of triangle
b = 4                           # side of triangle
c = math.sqrt(a**2 + b**2)      # hypotenuse
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')

# functions
def pythagoras (a, b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))
print(pythagoras(1, 1))

# practice
def signswitch(a):
	return (a * -1)
print (signswitch(10))
print (signswitch(-2))

def areacirc(r):                                           # area of a circle 
	if r <= 0: sys.exit('error: r must be greater than 0') # r = radius of circle
	return (math.pi * r**2)
print(areacirc(4))

def volrect(l, w, h): 			                           # volume of a rectangle
	if l <= 0: sys.exit('error: l must be greater than 0') # l = length
	if w <= 0: sys.exit('error: w must be greater than 0') # w = width
	if h <= 0: sys.exit('error: h must be greater than 0') # h = height
	return (l * w * h)
print(volrect(3, 2, 8))

def sacylinder(r, h): 			                           # surface area of a cylinder
	if r <= 0: sys.exit('error: r must be greater than 0') # r = radius
	if h <= 0: sys.exit('error: h must be greater than 0') # h = height
	return (2 * math.pi * r * h)
print(sacylinder(4, 9))

def celciuskelvin(c): 			                           # convert celcius to kelvin
	return (c + 273)                                       # c = temp in celcius
print(celciuskelvin(25))

def fahrenheitcelcius(f): 		                          # convert fahrenheit to celcius
	return ((f - 32) * (5 / 9))                           # f = temp in fahrenheit
print(fahrenheitcelcius(100))

def mphkph(m): 					                          # convert mph to kph
	if m < 0: sys.exit('error: m must be greater than 0') # m = speed in mph
	return (m * 1.609)
print(mphkph(65))

def fpsmph(f): 					                          # convert fps to mph
	if f < 0: sys.exit('error: f must be greater than 0') # f = speed in fps
	return (f * (3600 / 5280))
print(fpsmph(100))

def concdna(o): 				                         # find [DNA] from OD260
	return print(o * 50) 		                         # o = optical density at 260 nm
concdna(2)

def disxy(x1, y1, x2, y2):                               # find distance between 2 points
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(disxy(3, 0, 0, 4))

def midpoint(x1, y1, x2, y2):                           # find midpoint between 2 points
	mx = (x1 + x2) / 2
	my = (y1 + y2) / 2
	return mx, my
print(midpoint(2, 6, 4, 4))

# conditionals
a = 2
b = 3
if a == b:
	print('a equals b')
print(a, b)

# Boolean
c = a == b
print(c)
print(type(c))

# if-elif-else
d = 4
e = 4
if   d < e: print('d < e')
elif d > e: print('d > e')
else:       print('d == e')

# chaining
f = 1
g = 11
if f < g or f > g: print('all things being equal, a and b are not')
if f < g and f > g: print('you are living in a strange world')
if not False: print(True)

# floating point warning
h = 0.3
j = 0.1 * 3
if   h < j: print('h < j')
elif h > j: print('h > j')
else:       print('h == j')

print(abs(h -j))
if abs(h - j) < 1e-9: print('close enough')

if math.isclose(h, j): print('close enough')

# string comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# more practice
def is_integer(n):
	if n == n // 1: return True
	return False
print(is_integer(2))
print(is_integer(2.1))

def is_odd(n):
	if (n%2) != 0: return True
	return False
print(is_odd(36))
print(is_odd(37))

def is_pvalid(p):
	if p >= 0 and p <= 1: return True
	return False
print(is_pvalid(-0.89))
print(is_pvalid(0))
print(is_pvalid(0.3))
print(is_pvalid(1))
print(is_pvalid(1.26))

def mw_nt(nt):
	if   nt == 'A': return '135 g/mol'
	elif nt == 'G': return '151 g/mol'
	elif nt == 'C': return '111 g/mol'
	elif nt == 'T': return '126 g/mol'
	else:           sys.exit('unknown nucleotide')
print(mw_nt('A'))
print(mw_nt('W'))

def complement_nt(nt):
	if   nt == 'A': return 'T'
	elif nt == 'T': return 'A'
	elif nt == 'G': return 'C'
	elif nt == 'C': return 'G'
	else:           sys.exit('unknown nucleotide')
print(complement_nt('T'))
print(complement_nt('A'))
print(complement_nt('P'))