#include <iostream>

using namespace std;

// Define the structure of a node in the linked list
struct Node {
    int data;
    Node* next;
};

// Function to insert a new node at the beginning of the linked list
void insertAtBeginning(Node*& head, int newData) {
    // Create a new node
    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = head;

    // Update head to point to the new node
    head = newNode;
}

// Function to display the linked list
void displayList(Node* head) {
    while (head != nullptr) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Initialize an empty linked list
    Node* head = nullptr;

    // Insert some elements into the linked list
    insertAtBeginning(head, 3);
    insertAtBeginning(head, 7);
    insertAtBeginning(head, 11);

    // Display the linked list
    cout << "Linked List: ";
    displayList(head);

    return 0;
}
