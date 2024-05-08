def patched_func(*args):
	global_list = []
	
	
	def main():
	    (h1, h2) = (int(x) for x in args[0].split())
	    (a, b) = (int(x) for x in args[1].split())
	    global_list.append(solver(h1, h2, a, b))
	
	def solver(h1, h2, a, b):
	    if (a <= b):
	        if ((a * 8) >= (h2 - h1)):
	            return 0
	        else:
	            return (- 1)
	    else:
	        h = (h1 + (a * 8))
	        if (h >= h2):
	            return 0
	        else:
	            dayClimb = (12 * (a - b))
	            return ((((h2 - h) - 1) // dayClimb) + 1)
	main()
	return global_list