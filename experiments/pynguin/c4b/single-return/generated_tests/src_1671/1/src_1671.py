def func(*args):
	
	
	def isvowel(c):
	    vowels = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
	    for v in vowels:
	        if (c.lower() == v):
	            return True
	    return False
	s = args[0]
	min = 0
	maior = 0
	for i in s:
	    if isvowel(i):
	        min += 1
	        if (min > maior):
	            maior = min
	    else:
	        min = 0
	return((maior + 1))
