class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        chain = self.table[index]
        for i, pair in enumerate(chain):
            if pair[0] == key:
                chain[i] = (key, value)
                print(f"Updated key {key} with new value '{value}' at index {index}")
                return
        chain.append((key, value))
        print(f"Inserted ({key}, '{value}') at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        chain = self.table[index]
        for k, v in chain:
            if k == key:
                print(f"Found key {key} with value '{v}' at index {index}")
                return v
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        chain = self.table[index]
        for pair in chain:
            if pair[0] == key:
                chain.remove(pair)
                print(f"Deleted key {key} from index {index}")
                return
        print(f"Key {key} not found. Cannot delete.")

    def display(self):
        print("\n--- Hash Table ---")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print("------------------\n")


if __name__ == "__main__":
    h = HashTable()
    while True:
        print("1. Insert  2. Search  3. Delete  4. Display  5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            key = int(input("Enter key (integer): "))
            value = input("Enter value: ")
            h.insert(key, value)
        elif choice == '2':
            key = int(input("Enter key to search: "))
            h.search(key)
        elif choice == '3':
            key = int(input("Enter key to delete: "))
            h.delete(key)
        elif choice == '4':
            h.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.\n")
