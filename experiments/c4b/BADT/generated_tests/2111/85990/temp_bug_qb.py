def original_func(*args):
	global_list = []
	
	n = int(args[0])
	PRList = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump']
	global_list.append(PRList[n])
	return global_list