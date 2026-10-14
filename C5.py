def star_to_delta(ra, rb, rc):
    r_numerator = (ra * rb) + (rb * rc) + (rc * ra)
    
    rab = r_numerator / rc
    rbc = r_numerator / ra
    rca = r_numerator / rb
    
    return round(rab, 2), round(rbc, 2), round(rca, 2)
    
print("star_to_delta(10, 20, 30) -> ", star_to_delta(10, 20, 30))