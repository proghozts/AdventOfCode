filename  = 'Input/Day 1 Input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

def code_crack(list, start = 50):
    count = 0
    for i in list:
        if i[0] == 'R':
            start += int(i[1:])
            if start >= 100:
                count += start // 100
        else:
            prev = start
            start -= int(i[1:])
            if start <= 0:
                count += start // -100 + 1
                if prev == 0:
                    count -= 1
        start = start % 100

    return str(count)

print(code_crack(lines))
