#include <iostream>
using namespace std;

#define SIZE 10

class HashTable {
private:
    int table[SIZE];
    bool occupied[SIZE];

public:
    HashTable() {
        for (int i = 0; i < SIZE; i++) {
            table[i] = -1;
            occupied[i] = false;
        }
    }

    int hashFunction(int key) {
        return key % SIZE;
    }

    void insert(int key) {
        int index = hashFunction(key);
        int originalIndex = index;
        int i = 0;
        while (occupied[index] && i < SIZE) {
            index = (originalIndex + ++i) % SIZE;
        }
        if (i == SIZE) {
            cout << "Hash Table is full. Cannot insert " << key << endl;
            return;
        }
        table[index] = key;
        occupied[index] = true;
        cout << "Inserted key " << key << " at index " << index << endl;
    }

    void search(int key) {
        int index = hashFunction(key);
        int originalIndex = index;
        int i = 0;
        while (occupied[index] && i < SIZE) {
            if (table[index] == key) {
                cout << "Key " << key << " found at index " << index << endl;
                return;
            }
            index = (originalIndex + ++i) % SIZE;
        }
        cout << "Key " << key << " not found." << endl;
    }

    void remove(int key) {
        int index = hashFunction(key);
        int originalIndex = index;
        int i = 0;
        while (occupied[index] && i < SIZE) {
            if (table[index] == key) {
                table[index] = -1;
                occupied[index] = false;
                cout << "Deleted key " << key << " from index " << index << endl;
                return;
            }
            index = (originalIndex + ++i) % SIZE;
        }
        cout << "Key " << key << " not found. Cannot delete." << endl;
    }

    void display() {
        cout << "\n--- Hash Table ---\n";
        for (int i = 0; i < SIZE; i++) {
            if (occupied[i])
                cout << "Index " << i << " : " << table[i] << endl;
            else
                cout << "Index " << i << " : (empty)" << endl;
        }
        cout << "-------------------\n";
    }
};

int main() {
    HashTable ht;
    int choice, key;

    while (true) {
        cout << "\n1. Insert  2. Search  3. Delete  4. Display  5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter key to insert: ";
            cin >> key;
            ht.insert(key);
            break;
        case 2:
            cout << "Enter key to search: ";
            cin >> key;
            ht.search(key);
            break;
        case 3:
            cout << "Enter key to delete: ";
            cin >> key;
            ht.remove(key);
            break;
        case 4:
            ht.display();
            break;
        case 5:
            cout << "Exiting program." << endl;
            return 0;
        default:
            cout << "Invalid choice! Try again.\n";
        }
    }
    return 0;
}
