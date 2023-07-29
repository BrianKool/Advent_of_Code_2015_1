

file = open('input.txt', 'r')
result = 0

while 1:
    char = file.read(1)
    if char == "(":
        result +=1
    elif char == ")":
        result -=1
    else:
        break

print(result)

file.close()