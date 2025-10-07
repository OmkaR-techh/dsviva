#include <iostream>
#include <queue>
#include <string>
using namespace std;

class EventSystem {
    queue<string> events;
public:
    void addEvent(string event) {
        events.push(event);
        cout << "✅ Event \"" << event << "\" added to the queue.\n";
    }

    void processEvent() {
        if (events.empty()) {
            cout << "⚠️ No events to process.\n";
            return;
        }
        cout << "🎯 Processing event: " << events.front() << "\n";
        events.pop();
    }

    void displayEvents() {
        if (events.empty()) {
            cout << "No pending events.\n";
            return;
        }
        cout << "\n--- Pending Events ---\n";
        queue<string> temp = events;
        int i = 1;
        while (!temp.empty()) {
            cout << i++ << ". " << temp.front() << "\n";
            temp.pop();
        }
        cout << "----------------------\n";
    }

    void cancelEvent(string event) {
        if (events.empty()) {
            cout << "No events to cancel.\n";
            return;
        }
        queue<string> temp;
        bool found = false;
        while (!events.empty()) {
            if (events.front() == event) {
                found = true;
            } else {
                temp.push(events.front());
            }
            events.pop();
        }
        events = temp;
        if (found)
            cout << "❌ Event \"" << event << "\" canceled.\n";
        else
            cout << "⚠️ Event not found or already processed.\n";
    }
};

int main() {
    EventSystem system;
    int choice;
    string event;

    do {
        cout << "\n=== REAL-TIME EVENT SYSTEM ===\n";
        cout << "1. Add Event\n2. Process Next Event\n3. Display Pending Events\n4. Cancel Event\n5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore();

        switch (choice) {
        case 1:
            cout << "Enter event name: ";
            getline(cin, event);
            system.addEvent(event);
            break;
        case 2:
            system.processEvent();
            break;
        case 3:
            system.displayEvents();
            break;
        case 4:
            cout << "Enter event name to cancel: ";
            getline(cin, event);
            system.cancelEvent(event);
            break;
        case 5:
            cout << "Exiting system. Goodbye!\n";
            break;
        default:
            cout << "Invalid choice! Try again.\n";
        }
    } while (choice != 5);

    return 0;
}
