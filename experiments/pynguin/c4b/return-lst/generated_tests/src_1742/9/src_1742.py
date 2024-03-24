def func(*args):
	ret_values = []
	
	import fileinput
	
	def get_days(hc, ha, up, down):
	    if (hc >= ha):
	        return 0
	    return day_cycle(hc, ha, up, down)
	
	def day_cycle(hc, ha, up, down):
	    daynum = 0
	    while True:
	        if (daynum == 0):
	            hrs = 8
	        else:
	            hrs = 12
	        if ((hc + (up * hrs)) >= ha):
	            return daynum
	        else:
	            height_to_add = ((hrs * up) - (12 * down))
	            if ((height_to_add <= 0) and (daynum > 0)):
	                return (- 1)
	            else:
	                hc += height_to_add
	                daynum += 1
	if (__name__ == '__main__'):
	    args = []
	    for argline in fileinput.input():
	        pair = argline.split(' ')
	        pair = list((int(pair[0]), int(pair[1])))
	        args = (args + pair)
	    ret_values.append(get_days(*args))

	return ret_values
