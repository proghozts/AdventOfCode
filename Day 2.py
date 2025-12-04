with open(r"Input/Day 2 input.txt") as f:
    data = f.read().strip().split(",")


def IDCheck(input):
    total = 0
    for i in input:
        a, b = i.split('-')
        a = int(a)
        b = int(b)
        for y in range(a, b+1):
            s = str(y)
            l = len(s)
            if l % 2 == 0:
                mid = l // 2
                if s[:mid] == s[mid:]:
                    total += int(y)
                else:
                    pass
    return total

test = ['11-22']
print(IDCheck(data))

def IDCheck2(input):
    total = 0
    for i in input:
        a, b = i.split('-')
        a = int(a)
        b = int(b)
        for y in range(a, b+1):
            s = str(y)
            l = len(s)
            for x in range(2, l+1):
                if l % x == 0:
                    split = s[:l//x]
                    if split*x == s:
                        total += y
                        break
    return total       
                    
print(IDCheck2(data))