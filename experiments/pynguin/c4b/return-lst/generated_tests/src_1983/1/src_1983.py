def func(*args):
	ret_values = []
	
	
	def get_total_days(month):
	    if (month == 2):
	        return 28
	    if ((month == 7) or (month == 8)):
	        return 31
	    if ((month % 2) == 0):
	        if (month <= 7):
	            return 30
	        return 31
	    else:
	        if (month <= 7):
	            return 31
	        return 30
	
	def solve(month, weekday):
	    '\n    How many weeks are needed?\n\n    Month\n    1 = January\n    ...\n    12 = December\n\n    Weekday\n    1 = Monday\n    ...\n    7 = Sunday\n\n    January has 31 days.\n    The number of days alternate between 31 and 30 until December.\n    Two exceptions:\n        1. February has 28 days(29 in a leap year)\n        2. August skips alternation(July and August has 31 days)\n\n    Algorithm\n    1. Get days of the given month.\n    2. Days / 7 => minimum weeks\n    3. Days % 7 => remainder days\n    4. Compute additional weeks => Weekday + > 8 ? 2 : 1\n    '
	    days = get_total_days(month)
	    weeks = (days // 7)
	    remainder_days = (days % 7)
	    if ((weekday == 1) and (remainder_days == 0)):
	        return weeks
	    additional_weeks = (2 if ((weekday + remainder_days) > 8) else 1)
	    return (weeks + additional_weeks)
	
	def main():
	    (month, weekday) = args[0].split()
	    answer = solve(int(month), int(weekday))
	    ret_values.append(answer)
	    return answer
	if (__name__ == '__main__'):
	    main()

	return ret_values
