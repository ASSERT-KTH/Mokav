def func(*args):
	ret_values = []
	
	
	def render(input):
	    if (input[1:].upper() == input[1:]):
	        return input.swapcase()
	    return input
	ret_values.append(render(args[0]))

	return ret_values
