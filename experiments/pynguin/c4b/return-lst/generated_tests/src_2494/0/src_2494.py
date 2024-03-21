def func(*args):
	ret_values = []
	
	
	def main():
	    from string import ascii_uppercase as upp
	    s = args[0]
	    q = 0
	    q1 = 0
	    for i in s:
	        if (i in upp):
	            q += 1
	        else:
	            q1 += 1
	    if (q <= q1):
	        ret_values.append(s.lower())
	    else:
	        ret_values.append(s.upper())
	main()

	return ret_values
