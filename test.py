arr = [1,2,3,4,5]
N =len(arr)
K=3

grp1 = arr[K-1::-1]
grp2 = arr[:K-1:-1]

for i in range(len(grp2)):
    grp1.append(grp2[i])

for i in range(len(grp1)):
    print(grp1[i], end=" ")