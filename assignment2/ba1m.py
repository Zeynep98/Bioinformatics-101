Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def NumberToPattern(index, k):
	bases = ['A', 'C', 'G', 'T']
	pattern = ''
	for i in range(k):
		pattern += bases[index % 4]
		index = index // 4
	return pattern[::-1]

>>> print(NumberToPattern(5353,7))
CCATGGC
>>> 
