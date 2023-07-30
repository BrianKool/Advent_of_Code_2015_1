file = open('input.txt', 'r')
line = file.readline()

x=500
y=500
result = 0

community = [[0 for _ in range(1000)] for _ in range(1000)]
community[x][y] += 1

for i in line:
    match i:
        case ">":
            x+=1
            community[x][y] += 1
        case "<":
            x-=1
            community[x][y] += 1
        case "^":
            y+=1 
            community[x][y] += 1
        case "v":
            y-=1
            community[x][y] += 1
        case _:
            break


for x in range(1000):
    for y in range(1000):
        if community[x][y] >= 1:
            result += 1

print(result)
