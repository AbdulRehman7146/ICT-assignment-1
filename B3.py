readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count = 0
highest = readings [0]
lowest = readings [0]
total_sum = 0
total_count = 0

for r in readings :
	if r > 3.2 :
		count += 1
	if r > highest:
		highest = r
	if r < lowest:
		lowest = r
		
total_sum += r
total_count = 1
average = total_sum / total_count

print("Readings above 3.2 V: ", count)
print("Highest :", highest,"V")
print("Lowest :", lowest,"V")
print("Average :", average,"V")