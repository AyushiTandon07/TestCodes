
num = int(input('enter the number for factorial'))
ran=range(num,1,-1)
returned=1

for i in ran:
    returned=returned*i

print(returned)
