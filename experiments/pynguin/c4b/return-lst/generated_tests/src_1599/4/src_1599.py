def func(*args):
	ret_values = []
	
	(total_pages_nr, min_pages_per_day, max_pages_per_day, delta, reread_pages_nr) = (int(x) for x in args[0].split())
	days_nr = 0
	pages_read_nr = 0
	curr_speed = min_pages_per_day
	flag = False
	while (pages_read_nr < total_pages_nr):
	    if flag:
	        pages_read_nr -= reread_pages_nr
	    flag = True
	    pages_read_nr = max(curr_speed, (pages_read_nr + curr_speed))
	    curr_speed += delta
	    if (curr_speed > max_pages_per_day):
	        curr_speed = max_pages_per_day
	    days_nr += 1
	ret_values.append(days_nr)

	return ret_values
