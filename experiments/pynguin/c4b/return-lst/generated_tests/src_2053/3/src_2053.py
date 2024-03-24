def func(*args):
	ret_values = []
	
	from fractions import Fraction
	
	def Probability(ls):
	    (Y, W) = ls
	    num = (7 - max(Y, W))
	    if (num == 6):
	        return '1/1'
	    else:
	        return str(Fraction(num, 6))
	ret_values.append(Probability(list(map(int, args[0].split()))))

	return ret_values
