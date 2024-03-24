def func(*args):
	ret_values = []
	
	
	def main():
	    a = [eval(i) for i in args[0].split()]
	    a.sort()
	    if (((a[1] + a[2]) > a[3]) or ((a[0] + a[1]) > a[2])):
	        ret_values.append('TRIANGLE')
	    elif (((a[0] + a[1]) == a[2]) or ((a[0] + a[1]) == a[3]) or ((a[1] + a[2]) == a[3])):
	        ret_values.append('SEGMENT')
	    else:
	        ret_values.append('IMPOSSIBLE')
	main()

	return ret_values
