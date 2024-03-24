def func(*args):
	
	l = args[0]
	l = l.split(' ')
	q = int(l.pop())
	p = int(l.pop())
	b = int(l.pop())
	a = int(l.pop())
	n = int(l.pop())
	somme = 0
	'\n\nif p>q:\n\n    somme+=p*(n//a)\n\n    for j in range(1,(n//b)+1):\n\n            if (b*j)%a!=0:\n\n                somme+=q\n\nelse:\n\n    somme+=q*(n//b)\n\n    for j in range(1,(n//a)+1):\n\n            if (a*j)%b!=0:\n\n                somme+=p\n\n'
	
	def pgcd(x, y):
	    if (y == 0):
	        return x
	    else:
	        return pgcd(y, (x % y))
	d = pgcd(a, b)
	alpha = (a // d)
	beta = (b // d)
	if (p > q):
	    somme += (p * (n // a))
	    somme += (q * ((n // b) - ((n // b) // alpha)))
	else:
	    somme += (q * (n // b))
	    somme += (p * ((n // a) - ((n // a) // beta)))
	return(somme)
