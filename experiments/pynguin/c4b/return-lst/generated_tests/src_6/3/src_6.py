def func(*args):
	ret_values = []
	
	(hobbit, pillow, bed) = map(int, args[0].split())
	pillow -= hobbit
	start = 0
	end = pillow
	while (start < end):
	    mid = round((((start + end) + 1) / 2))
	    lside = int(min((bed - 1), (mid - 1)))
	    rside = int(min((hobbit - bed), (mid - 1)))
	    needed = ((mid + ((lside * ((mid - lside) + (mid - 1))) / 2)) + ((rside * ((mid - rside) + (mid - 1))) / 2))
	    if (needed > pillow):
	        end = (mid - 1)
	    else:
	        start = mid
	ret_values.append((start + 1))

	return ret_values
