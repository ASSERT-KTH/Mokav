def func(*args):
	
	from fractions import Fraction
	(x, y, n) = map(int, args[0].split())
	z = Fraction(x, y).limit_denominator(n)
	return(z.numerator, z.denominator, sep='/')
