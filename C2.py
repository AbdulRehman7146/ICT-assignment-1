def parallel_resistance(resistors):
    reciprocal_sum = 0

    for r in resistors:
        reciprocal_sum += 1 / r
       
    r_eq = 1 / reciprocal_sum
    return round(r_eq, 2) 

print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance[100, 200, 300] ->", parallel_resistance([100, 200, 300]))
