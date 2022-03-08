arr1 = []
n=int(input("enter the number of elements in array 1"))
for i in range(0,n):
    ele1=int(input())
    arr1.append(ele1)
arr2 = []
m=int(input("enter the number of elements in array 2"))
for j in range(0,m):
    ele2=int(input())
    arr2.append(ele2)
arr1.sort()
arr2.sort()
ans = (arr1 == arr2)
print(ans)