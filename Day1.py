#Day1
#written by : GW

with open(r"C:\Projects\Advent_of_Code\day1_data.txt", 'r') as data:
    lines = data.readlines()

elf = []
cal = []

for line in lines:
    if line != '\n':
        elf += [int(line)]
    else:
        cal += [sum(elf)]
        elf = []

print('Part 1: ', max(cal))

cal.sort(reverse=True)
print('Part 2: ', sum(cal[:3]))