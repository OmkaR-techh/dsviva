#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    string city;
    int population;
    Node* left;
    Node* right;

    Node(string c, int p) {
        city = c;
        population = p;
        left = right = NULL;
    }
};

// -----------------------------
// Iterative Insertion in BST
// -----------------------------
Node* insertCity(Node* root, string city, int population) {
    Node* newNode = new Node(city, population);

    if (root == NULL)
        return newNode; // empty tree

    Node* curr = root;
    Node* parent = NULL;

    while (curr != NULL) {
        parent = curr;
        if (city < curr->city)
            curr = curr->left;
        else if (city > curr->city)
            curr = curr->right;
        else {
            cout << "City already exists! Updating population.\n";
            curr->population = population;
            delete newNode;
            return root;
        }
    }

    if (city < parent->city)
        parent->left = newNode;
    else
        parent->right = newNode;

    return root;
}

// -----------------------------
// Search City (Iterative)
// -----------------------------
bool searchCity(Node* root, string city, int& comparisons) {
    Node* curr = root;
    comparisons = 0;

    while (curr != NULL) {
        comparisons++;
        if (curr->city == city) {
            cout << "City found! Population: " << curr->population << endl;
            return true;
        } else if (city < curr->city)
            curr = curr->left;
        else
            curr = curr->right;
    }

    return false;
}

// -----------------------------
// Update City Population (Iterative)
// -----------------------------
void updatePopulation(Node* root, string city, int newPop) {
    Node* curr = root;
    while (curr != NULL) {
        if (curr->city == city) {
            curr->population = newPop;
            cout << "Population updated successfully!\n";
            return;
        } else if (city < curr->city)
            curr = curr->left;
        else
            curr = curr->right;
    }
    cout << "City not found!\n";
}

// -----------------------------
// Delete a City (Iterative)
// -----------------------------
Node* deleteCity(Node* root, string city) {
    Node* curr = root;
    Node* parent = NULL;

    // Step 1: Find the node to delete
    while (curr != NULL && curr->city != city) {
        parent = curr;
        if (city < curr->city)
            curr = curr->left;
        else
            curr = curr->right;
    }

    // If node not found
    if (curr == NULL) {
        cout << "City not found!" << endl;
        return root;
    }

    // ==============================
    // CASE 1: Node with ZERO children
    // ==============================
    if (curr->left == NULL && curr->right == NULL) {
        // If deleting root node
        if (parent == NULL) {
            delete curr;
            return NULL; // Tree becomes empty
        }

        // Disconnect leaf node from parent
        if (parent->left == curr)
            parent->left = NULL;
        else
            parent->right = NULL;

        delete curr;
    }

    // ==============================
    // CASE 2: Node with ONE child
    // ==============================
    else if (curr->left == NULL || curr->right == NULL) {
        Node* child;
        if (curr->left != NULL)
            child = curr->left;
        else
            child = curr->right;

        // If deleting root node
        if (parent == NULL) {
            delete curr;
            return child; // Child becomes new root
        }

        // Connect parent directly to the child
        if (parent->left == curr)
            parent->left = child;
        else
            parent->right = child;

        delete curr;
    }

    // ==============================
    // CASE 3: Node with TWO children
    // ==============================
    else {
        // Find inorder successor (next bigger node)
        Node* curr1 = curr->right;
        Node* parent1 = curr;

        // Go to leftmost node in right subtree
        while (curr1->left != NULL) {
            parent1 = curr1;
            curr1 = curr1->left;
        }

        // Copy successor's data into current node
        curr->city = curr1->city;
        curr->population = curr1->population;

        // Delete the inorder successor node
        if (parent1->left == curr1)
            parent1->left = curr1->right;
        else
            parent1->right = curr1->right;

        delete curr1;
    }

    return root;
}


// -----------------------------
// Iterative Inorder Traversal (Ascending Order)
// -----------------------------
void displayAscending(Node* root) {
    Node* stack[100];
    int top = -1;
    Node* curr = root;

    if (root == NULL) {
        cout << "No cities in record.\n";
        return;
    }

    cout << "\nCities in Ascending Order:\n";

    while (curr != NULL || top != -1) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        cout << curr->city << " (" << curr->population << ")\n";
        curr = curr->right;
    }
}

// -----------------------------
// Iterative Reverse Inorder Traversal (Descending Order)
// -----------------------------
void displayDescending(Node* root) {
    Node* stack[100];
    int top = -1;
    Node* curr = root;

    if (root == NULL) {
        cout << "No cities in record.\n";
        return;
    }

    cout << "\nCities in Descending Order:\n";

    while (curr != NULL || top != -1) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->right;
        }
        curr = stack[top--];
        cout << curr->city << " (" << curr->population << ")\n";
        curr = curr->left;
    }
}

// -----------------------------
// Input Function
// -----------------------------
void takeInput(Node*& root) {
    string city;
    int population;
    cout << "Enter city name and population (-1 to stop): ";
    while (true) {
        cin >> city;
        if (city == "-1")
            break;
        cin >> population;
        root = insertCity(root, city, population);
    }
}

// -----------------------------
// Main Function
// -----------------------------
int main() {
    Node* root = NULL;
    int choice, population, comparisons;
    string city;

    do {
        cout << "\n----------------------------";
        cout << "\n CITY POPULATION MANAGEMENT ";
        cout << "\n----------------------------";
        cout << "\n1. Add City";
        cout << "\n2. Delete City";
        cout << "\n3. Update Population";
        cout << "\n4. Display Cities (Ascending)";
        cout << "\n5. Display Cities (Descending)";
        cout << "\n6. Search City";
        cout << "\n7. Exit";
        cout << "\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter city name: ";
            cin >> city;
            cout << "Enter population: ";
            cin >> population;
            root = insertCity(root, city, population);
            break;

        case 2:
            cout << "Enter city name to delete: ";
            cin >> city;
            root = deleteCity(root, city);
            break;

        case 3:
            cout << "Enter city name to update: ";
            cin >> city;
            cout << "Enter new population: ";
            cin >> population;
            updatePopulation(root, city, population);
            break;

        case 4:
            displayAscending(root);
            break;

        case 5:
            displayDescending(root);
            break;

        case 6:
            cout << "Enter city name to search: ";
            cin >> city;
            if (searchCity(root, city, comparisons))
                cout << "Comparisons made: " << comparisons << endl;
            else
                cout << "City not found! Comparisons made: " << comparisons << endl;
            break;

        case 7:
            cout << "Exiting program...\n";
            break;

        default:
            cout << "Invalid choice! Try again.\n";
        }

    } while (choice != 7);

    return 0;
}
