def linear_search(records, target_name):
    for index in range(len(records)):
        if records[index][0].lower() == target_name.lower():
            return index
    return -1

def binary_search(records, target_name):
    low = 0
    high = len(records) - 1
    while low <= high:
        mid = low + (high - low) // 2
        current_name = records[mid][0].lower()
        if current_name == target_name.lower():
            return mid
        elif current_name < target_name.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    print("===== E-Commerce Customer Records =====")
    n = int(input("Enter the number of friends/customers: "))

    records = []
    print("\nEnter details (Name and Mobile Number):")
    for i in range(n):
        name = input(f"Enter name of friend {i + 1}: ")
        mobile = input(f"Enter mobile number of {name}: ")
        records.append((name, mobile))

    records.sort(key=lambda x: x[0].lower())

    print("\n--- Customer Records ---")
    for i, (name, mobile) in enumerate(records):
        print(f"{i + 1}. Name: {name}, Mobile: {mobile}")

    print("\n===== LINEAR SEARCH =====")
    search_name = input("Enter the name to search (Linear Search): ")
    index = linear_search(records, search_name)
    if index != -1:
        print(f"Record Found at position {index + 1}: Name = {records[index][0]}, Mobile = {records[index][1]}")
    else:
        print("Record NOT found!")

    print("\n===== BINARY SEARCH =====")
    search_name = input("Enter the name to search (Binary Search): ")
    index = binary_search(records, search_name)
    if index != -1:
        print(f"Record Found at position {index + 1}: Name = {records[index][0]}, Mobile = {records[index][1]}")
    else:
        print("Record NOT found!")

if __name__ == "__main__":
    main()
