def func(*args):
	
	
	def caps():
	    string = args[0]
	    First_judge = 0
	    judge_count = 0
	    new_string = ''
	    new_string += string[0].upper()
	    if (string[0].upper() == string[0]):
	        First_judge = 1
	    for i in range(1, len(string)):
	        if (string[i].lower() == string[i]):
	            judge_count += 1
	        else:
	            judge_count += 0
	        new_string += string[i].lower()
	    if ((First_judge == 1) and (judge_count == 0)):
	        return string.lower()
	    elif ((First_judge == 1) and (judge_count < (len(string) - 1))):
	        return string
	    elif ((First_judge == 0) and (judge_count != 0)):
	        return string
	    else:
	        return new_string
	return(caps())
