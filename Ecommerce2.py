customer_id = []
b = int(input("Enter the number of IDs you want to enter: "))

# Taking IDs from user
for i in range(b):
    p = int(input(f"Enter ID number {i+1}: "))
    customer_id.append(p)

# Linear Search
def linear_search(customer_id, key):
    for i in range(len(customer_id)):
        if key == customer_id[i]:
            return i
    return -1

# Binary Search
def binary_search(customer_id, key):
    customer_id.sort()  # Important for binary search
    low, high = 0, len(customer_id) - 1
    while low <= high:
        mid = (low + high) // 2
        if customer_id[mid] == key:
            return mid
        elif customer_id[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Customer IDs:", customer_id)

# Ask for search method
search_type = int(input("\nEnter the type of search you want:\n1. Linear Search\n2. Binary Search\n"))

key = int(input("Enter the customer ID you want to search: "))

# Perform search
if search_type == 1:
    result = linear_search(customer_id, key)
elif search_type == 2:
    result = binary_search(customer_id, key)
else:
    print("Invalid choice!")
    exit()

# Print result
if result != -1:
    print(f"Element {key} found at index: {result}")
else:
    print("Element not found!")
