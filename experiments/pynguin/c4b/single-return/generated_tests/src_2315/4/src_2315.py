def func(*args):
	
	
	def render(input):
	    ret = input.lower()
	    for vowel in 'aeiouy':
	        ret = ret.replace(vowel, '')
	    ret = map((lambda c: ('.' + c)), ret)
	    return ''.join(ret)
	
	def main():
	    return(render(args[0]))
	main()
