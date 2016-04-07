current = 1
addifier = 1
counter = 3
while(1):
	print counter, len(str(current+addifier))
	old_current = current
	current += addifier
	addifier = old_current
	counter += 1
	if len(str(current+addifier)) > 1000:
		break
	