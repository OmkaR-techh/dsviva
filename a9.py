#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int d) {
        data = d;
        left = right = NULL;
    }
};

// -----------------------------
// Iterative Insertion in BST
// -----------------------------
Node* insertIntoBST(Node* root, int d) {
    Node* newNode = new Node(d);

    if (root == NULL)
        return newNode;  // empty tree

    Node* curr = root;
    Node* parent = NULL;

    while (curr != NULL) {
        parent = curr;
        if (d < curr->data)
            curr = curr->left;
        else
            curr = curr->right;
    }

    if (d < parent->data)
        parent->left = newNode;
    else
        parent->right = newNode;

    return root;
}

// -----------------------------
// Search in BST (Iterative)
// -----------------------------
bool searchBST(Node* root, int key) {
    Node* curr = root;
    while (curr != NULL) {
        if (curr->data == key)
            return true;
        else if (key < curr->data)
            curr = curr->left;
        else
            curr = curr->right;
    }
    return false;
}

Node* deleteNode(Node* root, int key) {
    Node* curr = root;
    Node* parent = NULL;

    // Step 1: Find the node to delete
    while (curr != NULL && curr->data != key) {
        parent = curr;
        if (key < curr->data)
            curr = curr->left;
        else
            curr = curr->right;
    }

    // If node not found
    if (curr == NULL) {
        cout << "Node not found!" << endl;
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
        Node* curr1 = curr->right;  // nextNode → curr1
        Node* parent1 = curr;       // parentOfNext → parent1

        // Go to leftmost node in right subtree
        while (curr1->left != NULL) {
            parent1 = curr1;
            curr1 = curr1->left;
        }

        // Copy successor's data into current node
        curr->data = curr1->data;

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
// Input Function (Iterative)
// -----------------------------
void takeInput(Node*& root) {
    int data;
    cout << "Enter values for BST (-1 to stop): ";
    while (cin >> data && data != -1) {
        root = insertIntoBST(root, data);
    }
}

// -----------------------------
// Iterative Inorder Traversal (LNR)
// -----------------------------
void inorder(Node* root) {
    Node* stack[50];
    int top = -1;
    Node* curr = root;

    cout << "\nInorder Traversal  : ";
    while (curr != NULL || top != -1) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        cout << curr->data << " ";
        curr = curr->right;
    }
}

// -----------------------------
// Iterative Preorder Traversal (NLR)
// -----------------------------
void preorder(Node* root) {
    if (root == NULL) return;

    Node* stack[50];
    int top = -1;

    stack[++top] = root;

    cout << "\nPreorder Traversal : ";

    while (top != -1) {
        Node* curr = stack[top--];
        cout << curr->data << " ";

        if (curr->right != NULL)
            stack[++top] = curr->right;
        if (curr->left != NULL)
            stack[++top] = curr->left;
    }
}

// -----------------------------
// Iterative Postorder Traversal (LRN)
// -----------------------------
void postorder(Node* root) {
    if (root == NULL) return;

    Node* stack1[50], *stack2[50];
    int top1 = -1, top2 = -1;

    stack1[++top1] = root;

    while (top1 != -1) {
        Node* curr = stack1[top1--];
        stack2[++top2] = curr;

        if (curr->left != NULL)
            stack1[++top1] = curr->left;
        if (curr->right != NULL)
            stack1[++top1] = curr->right;
    }

    cout << "\nPostorder Traversal: ";
    while (top2 != -1) {
        cout << stack2[top2--]->data << " ";
    }
}

// -----------------------------
// Main Function
// -----------------------------
int main() {
    Node* root = NULL;

    // Input values and build BST
    takeInput(root);

    // Perform all three traversals
    inorder(root);
    preorder(root);
    postorder(root);

    // -----------------------------
    // Search in BST
    // -----------------------------
    int key;
    cout << "\n\nEnter element to search: ";
    cin >> key;

    if (searchBST(root, key))
        cout << key << " found in BST.\n";
    else
        cout << key << " not found in BST.\n";

    // -----------------------------
    // Delete from BST
    // -----------------------------
    cout << "\nEnter element to delete: ";
    cin >> key;

    root = deleteNode(root, key);

    cout << "\nBST after deletion:";
    inorder(root);
    cout << endl;

    return 0;
}

