Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> seq = 'CTTCTCACGTACAACAAAATC'
>>> symbol2number = {"A":0,"C":1,"G":2,"T":3}
>>> def PatternToNumber(Pattern):
	if not Pattern:
		return 0
	symbol = Pattern[-1]
	prefix = Pattern[:-1]
	return ((4*PatternToNumber(prefix))+symbol2number[symbol])

>>> print(PatternToNumber(seq))
2161555804173
>>> 
