def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r
V_test = 12
R_test = 6

current = ohms_current(V_test, R_test)
power = power_dissipated(current, R_test)

print("Current = ", current, "A")
print("Power = ", power, "W")