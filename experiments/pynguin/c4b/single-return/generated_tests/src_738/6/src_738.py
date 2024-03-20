def func(*args):
	
	import itertools
	terms = list(map(int, args[0].split()))
	operators = args[1].split()
	
	def seek(terms, operators):
	    best = None
	    if (len(terms) == 1):
	        return terms[0]
	    for (i, a) in enumerate(terms):
	        for j in range((i + 1), len(terms)):
	            b = terms[j]
	            if (operators[0] == '+'):
	                x = (a + b)
	            else:
	                x = (a * b)
	            y = seek((((terms[:i] + terms[(i + 1):j]) + terms[(j + 1):]) + [x]), operators[1:])
	            if ((best == None) or (y < best)):
	                best = y
	    return best
	return(seek(terms, operators))
