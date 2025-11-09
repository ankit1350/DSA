# Function for Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Function for Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Function to display Top 5 Highest UNIQUE Salaries
def display_top_unique(sorted_salaries):
    unique_salaries = sorted(list(set(sorted_salaries)))  # remove duplicates
    count = min(5, len(unique_salaries))  # handle if less than 5 unique
    top_five = unique_salaries[-count:][::-1]  # pick highest unique salaries
    print(f"Top {count} highest UNIQUE salaries in the company:")
    print(top_five)


# Main Program
salaries = []
n = int(input("Enter total number of employees: "))

for i in range(n):
    sal = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

print("\nChoose Sorting Method:")
print("1. Selection Sort")
print("2. Bubble Sort")
choice = input("Enter your choice: ")

if choice == "1":
    sorted_salaries = selection_sort(salaries.copy())
    print("\nSalaries sorted using Selection Sort:")
elif choice == "2":
    sorted_salaries = bubble_sort(salaries.copy())
    print("\nSalaries sorted using Bubble Sort:")
else:
    print("Invalid choice.")
    
    

print(sorted_salaries)

# Display Top 5 Highest Unique Salaries
display_top_unique(sorted_salaries)
