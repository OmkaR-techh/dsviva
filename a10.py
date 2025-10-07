class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None

class CityBST:
    def __init__(self):
        self.root = None

    def insert(self, root, city, population):
        if root is None:
            return Node(city, population)
        if city.lower() < root.city.lower():
            root.left = self.insert(root.left, city, population)
        elif city.lower() > root.city.lower():
            root.right = self.insert(root.right, city, population)
        else:
            print("City already exists! Use Update option.")
        return root

    def search(self, root, city):
        comparisons = 0
        while root:
            comparisons += 1
            if city.lower() == root.city.lower():
                return root, comparisons
            elif city.lower() < root.city.lower():
                root = root.left
            else:
                root = root.right
        return None, comparisons

    def update_population(self, root, city, new_pop):
        node, comparisons = self.search(root, city)
        if node:
            node.population = new_pop
            print(f"Population for {city} updated to {new_pop}.")
        else:
            print(f"{city} not found.")
        print(f"Comparisons made: {comparisons}")

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, city):
        if root is None:
            return root
        if city.lower() < root.city.lower():
            root.left = self.delete(root.left, city)
        elif city.lower() > root.city.lower():
            root.right = self.delete(root.right, city)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.city, root.population = temp.city, temp.population
            root.right = self.delete(root.right, temp.city)
        return root

    def display_ascending(self, root):
        if root:
            self.display_ascending(root.left)
            print(f"{root.city} → Population: {root.population}")
            self.display_ascending(root.right)

    def display_descending(self, root):
        if root:
            self.display_descending(root.right)
            print(f"{root.city} → Population: {root.population}")
            self.display_descending(root.left)

bst = CityBST()
root = None

while True:
    print("\n--- City Population Management using BST ---")
    print("1. Add City")
    print("2. Delete City")
    print("3. Update Population")
    print("4. Display Cities Ascending")
    print("5. Display Cities Descending")
    print("6. Search City and Show Comparisons")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter city name: ")
        pop = int(input("Enter population: "))
        root = bst.insert(root, city, pop)

    elif choice == 2:
        city = input("Enter city name to delete: ")
        root = bst.delete(root, city)
        print("City deleted (if found).")

    elif choice == 3:
        city = input("Enter city name to update: ")
        new_pop = int(input("Enter new population: "))
        bst.update_population(root, city, new_pop)

    elif choice == 4:
        print("\nCities in Ascending Order:")
        bst.display_ascending(root)

    elif choice == 5:
        print("\nCities in Descending Order:")
        bst.display_descending(root)

    elif choice == 6:
        city = input("Enter city name to search: ")
        node, comp = bst.search(root, city)
        if node:
            print(f"City found! {city} → Population: {node.population}")
        else:
            print("City not found!")
        print(f"Comparisons made: {comp}")

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
