def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries

def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

def main():
    print("===== Employee Salary Sorting System =====")
    n = int(input("Enter number of employees: "))
    salaries = []

    for i in range(n):
        sal = float(input(f"Enter salary of employee {i + 1}: "))
        salaries.append(sal)

    salaries_bubble = salaries.copy()
    salaries_selection = salaries.copy()

    print("\nSorting using Bubble Sort...")
    bubble_sorted = bubble_sort(salaries_bubble)
    print("Salaries after Bubble Sort (Ascending):")
    print(bubble_sorted)

    print("\nSorting using Selection Sort...")
    selection_sorted = selection_sort(salaries_selection)
    print("Salaries after Selection Sort (Ascending):")
    print(selection_sorted)

    bubble_sorted.reverse()
    print("\nTop 5 highest salaries (from Bubble Sort result):")
    for sal in bubble_sorted[:5]:
        print(f"₹{sal:.2f}")

    print("\n===== End of Program =====")

if __name__ == "__main__":
    main()
