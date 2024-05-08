def patched_func(*args):
	global_list = []
	
	
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
	        global_list.append(s.lower())
	    else:
	        global_list.append(s.upper())
	main()
	return global_list