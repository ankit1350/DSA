def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
          
arr=[]
a=int(input("enter the number of elements you want in your array:"))
for _ in range(a):
    p=int(input("enter the element:"))
    arr.append(p)
selection_sort(arr)

print(arr)