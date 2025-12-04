with open(r"Input/Day 3 input.txt") as f:
    data = f.read().split("\n")

testlist = ['987654321111111','811111111111119','234234234234278','818181911112111']

def largeVolt(input):
    total = 0
    for i in input:
        l = len(i)
        big = 0
        bigg = 0
        for x in range(0, l):
            if (int(i[x]) > big) and x != l-1:
                    big = int(i[x])
                    bigg = 0
            elif (int(i[x]) > bigg) and x != 0:
                bigg = int(i[x])
            else:
                pass
        total += int(str(big)+str(bigg))
    return total

print(largeVolt(data))
            

def largeVolt2(input):
    total = 0
    for i in input:
        l = len(i)
        voltage = []
        p1 = 0
        while len(voltage) < 12:
            
            largestNum = 0
            for x in range(p1, l+1 - (12 - len(voltage))):
                num = int(i[x])
                if num > largestNum:
                    largestNum = num
                    p1 = x+1
                else:
                    pass
            voltage.append(largestNum)

        battery = ''
        for i in voltage:
            battery = battery + str(i)
        total += int(battery)
    
    return total



print(largeVolt2(data))