def func(*args):
	ret_values = []
	
	
	def main():
	    nums = list(map(int, args[0].split()))
	    a = ((nums[0] * nums[1]) + (nums[3] * 2))
	    b = ((nums[0] * nums[2]) + (nums[4] * 2))
	    if (a < b):
	        ret_values.append('First')
	    elif (a == b):
	        ret_values.append('Friendship')
	    else:
	        ret_values.append('Second')
	if (__name__ == '__main__'):
	    main()

	return ret_values
