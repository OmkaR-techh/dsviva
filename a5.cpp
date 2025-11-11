#include <iostream>
#include <string>
using namespace std;

class StudentNode {
public:
    int roll_no;
    string name;
    float marks;
    StudentNode* prev;
    StudentNode* next;

    StudentNode(int r, string n, float m) {
        roll_no = r;
        name = n;
        marks = m;
        prev = nullptr;
        next = nullptr;
    }
};

class StudentLinkedList {
private:
    StudentNode* head;

public:
    StudentLinkedList() {
        head = nullptr;
    }

    // Add student at end
    void add_student(int roll_no, string name, float marks) {
        StudentNode* new_node = new StudentNode(roll_no, name, marks);
        if (head == nullptr) {
            head = new_node;
        } else {
            StudentNode* temp = head;
            while (temp->next != nullptr)
                temp = temp->next;
            temp->next = new_node;
            new_node->prev = temp;
        }
        cout << "Student added successfully.\n";
    }

    // Delete student by roll number
    void delete_student(int roll_no) {
        StudentNode* temp = head;
        while (temp != nullptr) {
            if (temp->roll_no == roll_no) {
                if (temp->prev != nullptr)
                    temp->prev->next = temp->next;
                if (temp->next != nullptr)
                    temp->next->prev = temp->prev;
                if (temp == head)
                    head = temp->next;
                delete temp;
                cout << "Student deleted successfully.\n";
                return;
            }
            temp = temp->next;
        }
        cout << "Student not found.\n";
    }
    
    // Update student by roll number
    void update_student(int roll_no, string new_name, float new_marks) {
        StudentNode* temp = head;
        while (temp != nullptr) {
            if (temp->roll_no == roll_no) {
                temp->name = new_name;
                temp->marks = new_marks;
                cout << "Student updated successfully.\n";
                return;
            }
            temp = temp->next;
        }
        cout << "Student not found.\n";
    }

    // Search student by roll number
    void search_student(int roll_no) {
        StudentNode* temp = head;
        while (temp != nullptr) {
            if (temp->roll_no == roll_no) {
                cout << "Found -> Roll No: " << temp->roll_no
                     << ", Name: " << temp->name
                     << ", Marks: " << temp->marks << endl;
                return;
            }
            temp = temp->next;
        }
        cout << "Student not found.\n";
    }

    // Display all students
    void display_students() {
        if (head == nullptr) {
            cout << "No records to display.\n";
            return;
        }

        cout << "\nStudent Records:\n";
        cout << "Roll No\tName\tMarks\n";
        cout << "---------------------------\n";

        StudentNode* temp = head;
        while (temp != nullptr) {
            cout << temp->roll_no << "\t" << temp->name << "\t" << temp->marks << endl;
            temp = temp->next;
        }
    }

    // Sort students by roll number or marks
    void sort_students(string key, string order) {
        if (head == nullptr) {
            cout << "No records to sort.\n";
            return;
        }

        bool swapped;
        do {
            swapped = false;
            StudentNode* temp = head;
            while (temp->next != nullptr) {
                bool condition = false;

                if (key == "roll_no") {
                    condition = (order == "asc") ? 
                                (temp->roll_no > temp->next->roll_no) :
                                (temp->roll_no < temp->next->roll_no);
                } 
                else if (key == "marks") {
                    condition = (order == "asc") ?
                                (temp->marks > temp->next->marks) :
                                (temp->marks < temp->next->marks);
                } 
                else {
                    cout << "Invalid sort key. Use 'roll_no' or 'marks'.\n";
                    return;
                }

                if (condition) {
                    // Swap node data (not nodes)
                    int r = temp->roll_no;
                    string n = temp->name;
                    float m = temp->marks;

                    temp->roll_no = temp->next->roll_no;
                    temp->name = temp->next->name;
                    temp->marks = temp->next->marks;

                    temp->next->roll_no = r;
                    temp->next->name = n;
                    temp->next->marks = m;

                    swapped = true;
                }
                temp = temp->next;
            }
        } while (swapped);

        cout << "Records sorted by " << key << " in " << order << " order.\n";
    }
};

// ---------- Main Menu ----------
int main() {
    StudentLinkedList sll;
    int choice;

    while (true) {
        cout << "\n--- Student Record Management ---\n";
        cout << "1. Add Student\n";
        cout << "2. Delete Student\n";
        cout << "3. Update Student\n";
        cout << "4. Search Student\n";
        cout << "5. Display Students\n";
        cout << "6. Sort Students\n";
        cout << "7. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            int r;
            string n;
            float m;
            cout << "Enter Roll No: ";
            cin >> r;
            cout << "Enter Name: ";
            cin >> n;
            cout << "Enter Marks: ";
            cin >> m;
            sll.add_student(r, n, m);
        } 
        else if (choice == 2) {
            int r;
            cout << "Enter Roll No to delete: ";
            cin >> r;
            sll.delete_student(r);
        } 
        else if (choice == 3) {
            int r;
            string n;
            float m;
            cout << "Enter Roll No to update: ";
            cin >> r;
            cout << "Enter New Name: ";
            cin >> n;
            cout << "Enter New Marks: ";
            cin >> m;
            sll.update_student(r, n, m);
        } 
        else if (choice == 4) {
            int r;
            cout << "Enter Roll No to search: ";
            cin >> r;
            sll.search_student(r);
        } 
        else if (choice == 5) {
            sll.display_students();
        } 
        else if (choice == 6) {
            string k, o;
            cout << "Sort by (roll_no/marks): ";
            cin >> k;
            cout << "Order (asc/desc): ";
            cin >> o;
            sll.sort_students(k, o);
        } 
        else if (choice == 7) {
            cout << "Exiting...\n";
            break;
        } 
        else {
            cout << "Invalid choice! Try again.\n";
        }
    }

    return 0;
}
