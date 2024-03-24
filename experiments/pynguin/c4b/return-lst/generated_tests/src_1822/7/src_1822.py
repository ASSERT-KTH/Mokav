def func(*args):
	ret_values = []
	
	from fractions import Fraction
	(x, y, n) = map(int, args[0].split())
	z = Fraction(x, y).limit_denominator(n)
	ret_values.append(z.numerator, z.denominator, sep='/')

	return ret_values
