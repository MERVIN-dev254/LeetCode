# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr = [1,3,5]
arr1 = [2,4,6]

for i in arr1:
    arr.append(i)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
 
print(arr)           
if len(arr) % 2 == 0:
    median = (arr[len(arr)//2] + arr[(len(arr)//2) - 1]) / 2
else:
    median = arr[len(arr)//2]
    
print(median)
    