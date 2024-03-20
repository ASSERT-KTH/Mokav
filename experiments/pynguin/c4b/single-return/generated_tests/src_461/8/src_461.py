def func(*args):
	
	string = args[0]
	list_ = string.split()
	answer = []
	x = ((int(list_[0]) + int(list_[1])) * 2)
	answer.append(x)
	x = ((int(list_[0]) + int(list_[1])) + int(list_[2]))
	answer.append(x)
	x = ((int(list_[1]) + int(list_[2])) * 2)
	answer.append(x)
	x = ((int(list_[2]) + int(list_[0])) * 2)
	answer.append(x)
	return(min(answer))
