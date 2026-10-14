one = 0
five = 0
reject = 0

while True:
    r = float(input("Enter resistance (0 to stop): "))

    if r == 0:
        break

    if 99 <= r <= 101:
        one = one + 1

    elif 95 <= r <= 105:
        five = five + 1

    else:
        reject = reject + 1

print("1% tolerance:", one)
print("5% tolerance:", five)
print("Rejected:", reject)
