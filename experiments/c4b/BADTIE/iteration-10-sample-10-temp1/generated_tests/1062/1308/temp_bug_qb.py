def original_func(*args):
	global_list = []
	
	numb = args[0]
	luck = 0
	notluck = 0
	seven = 0
	four = 0
	for i in range(len(numb)):
	    if ((int(numb[i]) == 4) or (int(numb[i]) == 7)):
	        luck = (luck + 1)
	        if (numb[i] == 4):
	            four = (four + 1)
	        else:
	            seven = (seven + 1)
	    else:
	        notluck = (notluck + 1)
	if (((luck < notluck) and (luck > 0) and (notluck > 0)) or ((luck == len(numb)) and (luck > 1) and (four != (len(numb) - 1)) and (seven != (len(numb) - 1)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list