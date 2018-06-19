Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def hammingDistance(S, T):
	ham = 0
	for x, y in zip(S, T):
		if x != y:
			ham += 1
	return ham

>>> def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z
		distance += hamming
	return distance

>>> dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
>>> pattern = "AAA"
>>> print(distanceBetweenPatternAndString(pattern, dna))
5
>>> 
