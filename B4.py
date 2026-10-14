voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

count = 1
longest = 1

start = voltages[0]
end = voltages[0]
current_start = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        count = count + 1

        if count > longest:
            longest = count
            start = current_start
            end = voltages[i]

    else:
        count = 1
        current_start = voltages[i]

print("Longest continuous drop:", longest, "minutes")
print("Started at:", start, "V")
print("Ended at:", end, "V")
