class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append(None)
        self.deleted = "<del>"

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash_function(key)
        start = idx
        while self.table[idx] not in (None, self.deleted):
            if self.table[idx] == key:
                print("Key already exists")
                return
            idx = (idx + 1) % self.size
            if idx == start:
                print("Table full!")
                return
        self.table[idx] = key
        print("Inserted")

    def search(self, key):
        idx = self.hash_function(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx] == key:
                print(f"Found at index {idx}")
                return idx
            idx = (idx + 1) % self.size
            if idx == start:
                break
        print("Not found")
        return None

    def delete(self, key):
        idx = self.search(key)
        if idx is not None:
            self.table[idx] = self.deleted
            print("Deleted")

    def display(self):
        print("\nHash Table:")
        for i, val in enumerate(self.table):
            print(i,":", val)


if __name__ == "__main__":
    size = int(input("Enter table size: "))
    h = HashTable(size)

    while True:
        print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
        ch = int(input("Choice: "))
        if ch == 1:
            h.insert(int(input("Key: ")))
        elif ch == 2:
            h.search(int(input("Key: ")))
        elif ch == 3:
            h.delete(int(input("Key: ")))
        elif ch == 4:
            h.display()
        elif ch == 5:
            break
        else:
            print("Invalid")
