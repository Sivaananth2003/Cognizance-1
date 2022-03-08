a = [10,11,12,13,14]
first = 11
last= 13
final=[]
addZeros = False
for i in a:
    final.append(i)
    if i == first:
        addZeros = True
    if i == last:
        addZeros = False
    if addZeros:
        final.extend([0,0,0,0,0])
print(final) 