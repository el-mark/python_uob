aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
if target in aList:
    print(aList.index(target))
else:
    print(-1)

# this will pop an error
# print(aList.index(12))
