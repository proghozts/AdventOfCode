data = []

with open("Input/Day 6 Input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        data.append(parts)

def garbage(full):
    total = 0
    for i in range (len(full[0])):
        if full[4][i] == '*':
            total += int(full[0][i]) * int(full[1][i]) * int(full[2][i]) * int(full[3][i])
        elif full[4][i] == '+':
            total += int(full[0][i]) + int(full[1][i]) + int(full[2][i]) + int(full[3][i])

    return total

print(garbage(data))

testValue = [['123', '328', '51', '64'],
            ['45', '64', '387', '23'],
            ['6', '98', '215', '314'],
            ['*', '+', '*', '+']]



"""
def garbage2(full):
    total = 0
    for i in range (len(full[0])):
        tempList = [full[0][i], full[1][i], full[2][i], full[3][i]]
        tempList2 = ['','','']
        for j in tempList: #51
            
            for x in range(0, len(j)):
                tempList2[2-x] = str(tempList2[2-x]) + j[x]
        print(tempList2)
        tempValue = 1
        for z in tempList2:
            if z != '' and full[len(testValue)-1][i] == '*':
                tempValue *= int(z)
            elif z != '' and full[len(testValue)-1][i] == '+':
                tempValue += int(z)
        total += tempValue

    return total

print(garbage2test(testValue))
#print(garbage2(data))
"""

with open(r"Input/Day 6 input.txt") as f:
    data2 = f.read().split("\n")

def garbage2(full):
    total = 0
    tempList = []
    tempValue = 0
    for i in range(len(full[0])-1,-1,-1):
        if full[0][i] == ' ' and full[1][i] == ' ' and full[2][i] == ' ' and full[3][i] == ' ':
            continue
        if full[4][i] == ' ':
            tempList.append('' + full[0][i] + full[1][i] + full[2][i] +full[3][i])
            print(tempList)
        else:
            tempList.append('' + full[0][i] + full[1][i] + full[2][i] +full[3][i])
            print(tempList)
            if full[4][i] == '*':
                tempValue = 1
                for j in tempList:
                    tempValue *= int(j.strip())
                total += tempValue
                tempList = []
            elif full[4][i] == '+':
                tempValue = 0
                for j in tempList:
                    tempValue += int(j)
                total += tempValue
                tempList = []     
    return total               

print(garbage2(data2))

