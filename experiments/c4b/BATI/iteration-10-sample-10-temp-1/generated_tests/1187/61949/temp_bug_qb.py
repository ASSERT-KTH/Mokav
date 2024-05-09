def original_func(*args):
	global_list = []
	
	
	def render(input):
	    if (input[1:].upper() == input[1:]):
	        return (input[:1].upper() + input[1:].lower())
	    return input
	global_list.append(render(args[0]))
	return global_list