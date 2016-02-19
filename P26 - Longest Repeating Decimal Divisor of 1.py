

max_set= [0,0]

for divisor in range(1,1000):
	counter = 1
	current_denominator = 1
	remainder_list = []
	while(1):
		scaled_denominator = current_denominator
		while(scaled_denominator < divisor):
			scaled_denominator *= 10
		
		remainder = scaled_denominator % divisor
		#print scaled_denominator,divisor,remainder
		if(remainder == 0):
			print divisor, "not repeating"
			break
			
		elif(remainder in (remainder_list+[1,10,100,1000,current_denominator])):
			print divisor, "repeat detected. # Places:", counter
			if counter > max_set[0]:
				max_set = counter,divisor
			break
			
		else:
			remainder_list.append(remainder)
			current_denominator = remainder
			counter += 1
			
print max_set
			

	