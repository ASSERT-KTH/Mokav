def func(*args):
	ret_values = []
	
	
	def render(input):
	    ret = input.lower()
	    for vowel in 'aeiouy':
	        ret = ret.replace(vowel, '')
	    ret = map((lambda c: ('.' + c)), ret)
	    return ''.join(ret)
	
	def main():
	    ret_values.append(render(args[0]))
	main()

	return ret_values
