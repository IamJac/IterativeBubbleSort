from array import *
def bubble_sort(data_array):
    for i in range(len(data_array)):
        for j in range(i+1,len(data_array)):
            if data_array[j]<data_array[i]:
                data_array[i],data_array[j]=data_array[j],data_array[i]
data=array('i',[])
size=int(input("Input a non-negative size for the array"))
print("Input values into the array")
for r in range(size):
    nums=int(input())
    data.append(nums)
print()
print("Unsorted array elements")
for h in data:
    print(h,end=" ")
print()
bubble_sort(data)
print("Sorted array elements")
for e in data:
    print(e,end=" ")
