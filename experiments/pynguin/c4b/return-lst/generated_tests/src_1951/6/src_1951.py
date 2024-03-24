def func(*args):
	ret_values = []
	
	
	def football(a):
	    count = 1
	    b = a[0]
	    for number in a[1:len(a)]:
	        if (number == b):
	            count += 1
	        else:
	            count = 1
	        if (count == 7):
	            break
	        b = number
	    if (count == 7):
	        return 'YES'
	    else:
	        return 'NO'
	
	def main():
	    a = args[0]
	    b = football(a)
	    ret_values.append(b)
	if (__name__ == '__main__'):
	    main()

	return ret_values
