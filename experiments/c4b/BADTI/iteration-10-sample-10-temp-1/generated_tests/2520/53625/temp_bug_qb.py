def original_func(*args):
	global_list = []
	
	from fractions import Fraction
	
	def Probability(ls):
	    (Y, W) = ls
	    return str(Fraction((7 - max(Y, W)), 6))
	global_list.append(Probability(list(map(int, args[0].split()))))
	return global_list