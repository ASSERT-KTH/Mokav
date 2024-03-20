def func(*args):
	
	
	def main():
	    x = args[0]
	    y = int(x)
	    s = sum((int(d) for d in x))
	    for i in range(len(x)):
	        if (x[i] == '0'):
	            continue
	        z = ((x[:i] + str((int(x[i]) - 1))) + ('9' * ((len(x) - i) - 1)))
	        zi = int(z)
	        t = sum((int(d) for d in z))
	        if ((t > s) or ((t == s) and (zi > y))):
	            y = zi
	            s = t
	    return(y)
	if (__name__ == '__main__'):
	    main()
