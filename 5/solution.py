data = open("input.txt", "r")

list = data.readlines()
result = 0

def vowelscheck (item):
    count = 0
    for i in item:
        if i in 'aeiou':
            count += 1
    if count >= 3:
        return True
    return False

def matchrestrict(item):
    for x in range(0,len(item)-1):
        a = item[x]
        b = item[x+1]
        match (a+b):
                case "ab":
                    return False
                case "cd":
                    return False
                case "pq":
                    return False
                case "xy":
                    return False
                case _:
                    continue
    return True
    

def twoinrow (item):
    for x in range(0,len(item)-1):
        a = item[x]
        b = item[x+1]
        if a == b:
            # print("print twoinrow item")
            # print(item[x],item[x+1])
            # print("*************************")
            return True            
            
    return False
    


for i in list:
    # print("vowel check")
    # print(vowelscheck(i))
    # print("two in row")
    # print(twoinrow(i))
    # print("match restrict words")
    # print(matchrestrict(i))
    # print("----------------------")
    if vowelscheck(i) and twoinrow(i) and matchrestrict(i):
        result += 1
        
print(result)
