file = open('input.txt', 'r')

result = 0

def wrappapper(l,w,h):
    return 2*l*w+2*w*h+2*h*l+min(l*w,w*h,h*l)


line = file.read().splitlines()


for i in line:
    i = i.split("x") 
    result += wrappapper(int(i[0]),int(i[1]),int(i[2]))


print(result)


