# Day3
# written by : GW
import string

#Part 1

#create list of letters
alphabet = string.ascii_letters
#assign a value beginning from 1 to each letter, increasing by 1 (a-->z, A-->Z)
scores = {alphabet[i]: i+1 for i in range(len(alphabet))}
print(scores)

with open(r"C:\Projects\Advent_of_Code\day3_data.txt", 'r') as data:
    lines = data.readlines()
    lines = [i.rstrip('\n') for i in lines]

#for each line in lines, split line in the middle into two strings
rucksacks = [[line[:len(line) // 2], line[len(line) // 2:]] for line in lines]

shared_list = []
for i in range(len(rucksacks)):
    shared = [c for c in rucksacks[i][0] if c in rucksacks[i][1]]
    shared_list.append(shared)
    print("Value at position ", i,": ",shared_list)
#keep only the first item in the list
shared_list = [i[0] for i in shared_list]
print(shared_list)
#flatten list
shared_list = [item for sublist in shared_list for item in sublist]
print(shared_list)
#sum the value of shared_list based on scores
shared_list = sum([scores[i] for i in shared_list])

print('Part 1: ', shared_list)

#Part 2
alphabet = string.ascii_letters
#assign a value beginning from 1 to each letter, increasing by 1 (a-->z, A-->Z)
scores = {alphabet[i]: i+1 for i in range(len(alphabet))}
print(scores)

with open(r"C:\Projects\Advent_of_Code\day3_data.txt", 'r') as data:
    lines = data.readlines()
    lines = [i.rstrip('\n') for i in lines]

#find a character that is common to each group of 3 lines
shared_list = []
for i in range(0, len(lines), 3):
    shared = [c for c in lines[i] if c in lines[i+1] and c in lines[i+2]]
    shared_list.append(shared)
    print("Value at position ", i,": ",shared_list)
#keep only the first item in the list
shared_list = [i[0] for i in shared_list]
shared_list = sum([scores[i] for i in shared_list])
print(shared_list)