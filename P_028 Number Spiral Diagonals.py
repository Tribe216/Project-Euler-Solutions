
total_sum = 1
grid_size = 1001
for rc in range (2,grid_size,2):
	total_sum += ( 4*pow(rc,2) + (2*rc) + 4 )

print total_sum
