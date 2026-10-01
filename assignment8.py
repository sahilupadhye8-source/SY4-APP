# Open input file
file = open("input.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

first_two = lines[:2]

file.close()

output = open("output.txt", "w")

for line in first_two:
    output.write(line)

output.close()

print("First two lines written to output.txt")