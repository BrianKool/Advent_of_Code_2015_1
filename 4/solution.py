import hashlib


result = 0

for i in range(10000000000):
    result = hashlib.md5(("iwrupvqb"+str(i)).encode('utf-8')).hexdigest()
    if result[0:5:1] == "00000":
        print(result)
        print("answer is:")
        print(i)
        break
    