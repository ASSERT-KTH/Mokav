def patched_func(*args):
	global_list = []
	
	from fractions import Fraction
	
	def Probability(ls):
	    (Y, W) = ls
	    num = (7 - max(Y, W))
	    if (num == 6):
	        return '1/1'
	    else:
	        return str(Fraction(num, 6))
	global_list.append(Probability(list(map(int, args[0].split()))))
	return global_list