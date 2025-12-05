with open(r"Input/Day 5 Ingredients.txt") as f:
    ingredients = f.read().split("\n")

with open(r"Input/Day 5 Fresh.txt") as f:
    fresh = f.read().split("\n")

def ingredientCheck(ingredients, fresh):
    total = 0
    for i in ingredients:
        ing = int(i)
        for x in fresh:
            a, b = x.split('-')
            a = int(a)
            b = int(b)
            if ing >= a and ing <= b:
                total += 1
                break
    return total

print(ingredientCheck(ingredients, fresh)) 

freshTest = ["3-5", "10-14", "16-20", "12-18"]

def freshCheck(completed,a,b):
        for c in completed:
            c_a, c_b = c.split('-')
            c_a = int(c_a)
            c_b = int(c_b)
            if (c_a <= a <= c_b):
                a = c_b + 1
            if (c_a <= b <= c_b):
                b = c_a - 1
            if c_a < a and b < c_b:
                return [0]
            if a < c_a and c_b < b:
                return [freshCheck(completed, a, c_a - 1), freshCheck(completed, c_b + 1, b)]
        return [f"{a}-{b}", b - a + 1]
            


def freshTotal(fresh):
    total = 0
    completed = []
    for x in fresh:
        a, b = x.split('-')
        a = int(a)
        b = int(b)
        check = freshCheck(completed, a, b)
        if len(check) == 1:
            pass
        elif type(check[1]) != list:
            completed.append(check[0])
            total += check[1]
        else:
            completed.append(check[0][0])
            completed.append(check[1][0])
            total += check[1][1] + check[0][1]

    return total

print(freshTotal(fresh))