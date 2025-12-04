with open(r"Input/Day 4 input.txt") as f:
    data = f.read().split("\n")

testinput = ['..@@.@@@@.','@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@','.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']

def paperCheck(data):
    total = 0
    for row in range(0, len(data)):
        line = data[row]
        for x in range(0, len(line)):
            if line[x] == '@':
                counter = 0
                surround = [[row-1, x-1], [row-1, x], [row-1, x+1], [row, x-1], [row, x+1], [row+1, x-1], [row+1, x], [row+1, x+1]]
                for y in surround:
                    if 0 <= y[0] < len(data) and 0 <= y[1] < len(line):
                        if data[y[0]][y[1]] == '@':
                            counter += 1
                if counter < 4:
                    total += 1
            
    return total

#print(paperCheck(testinput))

#print(paperCheck(data))


def paperCheck2(data): #Yeah not my best solution // could hear my computer rev up the fan to run this
    data = [list(row) for row in data]
    total = 0
    changed = True
    while changed:
        changed = False
        for row in range(0, len(data)):
            for x in range(0, len(data[row])):
                if data[row][x] == '@':
                    counter = 0
                    surround = [[row-1, x-1], [row-1, x], [row-1, x+1], [row, x-1], [row, x+1], [row+1, x-1], [row+1, x], [row+1, x+1]]
                    for y in surround:
                        if 0 <= y[0] < len(data) and 0 <= y[1] < len(data[row]):
                            if data[y[0]][y[1]] == '@':
                                counter += 1
                    if counter < 4:
                        data[row][x] = '.'
                        total += 1
                        changed = True
                        break
            if changed:
                break
    return total

print(paperCheck2(data))
                    


        
