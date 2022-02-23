
l1 = []
l1 = [['Roll no','Student Name','Marks'], ['164','Tokyo','99'], ['165','Nairobi','100'], ['166','Berlin','99']]
for i in l1:
    print (i)
print("Creating a new record")
L2 = input("Enter the roll no "),input('Enter the name '),input('Enter the marks ')
l1.append(L2)
for j in l1:
    print(j)

l2 = int(input('Enter the record to be extracted: '))
if(l2>=5):
    print("Sorry input is greater than expected records")
else:
    print(l1[l2])