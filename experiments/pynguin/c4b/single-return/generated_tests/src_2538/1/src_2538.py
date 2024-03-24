def func(*args):
	
	from fractions import Fraction
	(x, y, n) = map(int, args[0].split(' '))
	res = Fraction(x, y).limit_denominator(n)
	return(res.numerator, res.denominator, sep='/')
