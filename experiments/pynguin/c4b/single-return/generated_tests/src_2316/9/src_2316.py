def func(*args):
	
	
	def render(input):
	    if (input[1:].upper() == input[1:]):
	        return input.swapcase()
	    return input
	return(render(args[0]))
