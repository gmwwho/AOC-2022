# Day2
# written by : GW

with open(r"C:\Projects\Advent_of_Code\day2_data.txt", 'r') as data:
    lines = data.readlines()

#Part 1
total_score = 0
scores = {'A': 1,   #A = Rock
        'B': 2,     #B = Paper
        'C': 3,     #C = Scissors

        'X': 1,     #X = Rock
        'Y': 2,     #Y = Paper
        'Z': 3}     #Z = Scissors

#compare the characters within the string  
for i in lines:
    i = i.strip('\n').split(' ') 
    if scores[i[0]] == scores[i[1]]: #rock vs rock, paper vs paper, scissors vs scissors
        total_score += scores[i[1]] + 3
        print('tie')
    elif scores[i[0]]==1 and scores[i[1]]==2: #rock vs paper
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==1 and scores[i[1]]==3: #rock vs scissors
        total_score += scores[i[1]]
        print('loss')
    elif scores[i[0]]==2 and scores[i[1]]==1: #paper vs rock
        total_score += scores[i[1]]
        print('loss')
    elif scores[i[0]]==2 and scores[i[1]]==3: #paper vs scissors
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==3 and scores[i[1]]==1: #scissors vs rock 
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==3 and scores[i[1]]==2: #scissors vs paper
        total_score += scores[i[1]]
        print('loss')
    
print('Score for Part1: ', total_score)

#Part 2

#x == loss
#y == tie
#z == win

total_score = 0

for i in lines:
    i = i.strip('\n').split(' ')
    if scores[i[1]] == 1: #make a loss
        if i[0] == 'A':
            i[1] = 'Z'
        elif i[0] == 'B':
            i[1] = 'X'
        elif i[0] == 'C':
            i[1] = 'Y'
        print('loss')
    elif scores[i[1]] == 2: #make a tie
        i[1] = i[0]
        print('tie')
    elif scores[i[1]] == 3: #make a win
        if i[0] == 'A':
            i[1] = 'Y'
        elif i[0] == 'B':
            i[1] = 'Z'
        elif i[0] == 'C':
            i[1] = 'X'
        print('win')

    #compare the characters within the string   
    if scores[i[0]] == scores[i[1]]: #rock vs rock, paper vs paper, scissors vs scissors
        total_score += scores[i[0]] + 3
        print('tie')

    elif scores[i[0]]==1 and scores[i[1]]==2: #rock vs paper
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==1 and scores[i[1]]==3: #rock vs scissors
        total_score += scores[i[1]]
        print('loss')
    elif scores[i[0]]==2 and scores[i[1]]==1: #paper vs rock
        total_score += scores[i[1]]
        print('loss')
    elif scores[i[0]]==2 and scores[i[1]]==3: #paper vs scissors
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==3 and scores[i[1]]==1: #scissors vs rock 
        total_score += scores[i[1]] + 6
        print('win')
    elif scores[i[0]]==3 and scores[i[1]]==2: #scissors vs paper
        total_score += scores[i[1]]
        print('loss')
    
print('Score for Part2: ', total_score)