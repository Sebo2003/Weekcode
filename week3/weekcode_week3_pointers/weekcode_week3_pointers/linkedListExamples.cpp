#include <iostream>
#include "linkedList.h"
using namespace std;

void insertAtBeginning(Node*& head, int newData) {
    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = head;
    head = newNode;
}

void insertAfter(Node* prevNode, int newData) {
    if (prevNode == nullptr) {
        std::cout << "Previous node cannot be null." << std::endl;
        return;
    }

    Node* newNode = new Node();
    newNode->data = newData;
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}

void displayList(Node* head) {
    while (head != nullptr) {
        std::cout << head->data << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

bool search(Node* head, int value) {
    Node* current = head;
    while (current != nullptr) {
        if (current->data == value) {
            return true; 
        }
        current = current->next;
    }
    return false; 
}

void deleteNode(Node*& head, int key) {
    if (head != nullptr && head->data == key) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return;
    }

    Node* prev = nullptr;
    Node* current = head;
    while (current != nullptr && current->data != key) {
        prev = current;
        current = current->next;
    }

    if (current == nullptr)
        return;

    prev->next = current->next;

    delete current;
}

void deleteTail(Node*& head) {
    if (head == nullptr) {
        return; 
    }
    else if (head->next == nullptr) {
        delete head; 
        head = nullptr;
        return;
    }

    Node* prev = nullptr;
    Node* current = head;

    while (current->next != nullptr) {
        prev = current;
        current = current->next;
    }

    delete current;
    prev->next = nullptr;
}


void pointerShowCase() {

    int x = 10;

    int* pointer = &x;

    cout << "*pointer (1): " << *pointer << endl;

    cout << "pointer (1): " << pointer << endl;

    cout << "&pointer (1): " << &pointer << endl;
    cout << endl;

    x = 20;

    cout << "*pointer (2): " << *pointer << endl;

    cout << "pointer (2): " << pointer << endl;

    cout << "&pointer (2): " << &pointer << endl;
    cout << endl;

    int y = 30;
    x = y;

    cout << "*pointer (3): " << *pointer << endl;

    cout << "pointer (3): " << pointer << endl;

    cout << "&pointer (3): " << &pointer << endl;
    cout << endl;

    pointer = &y;
    x = 5;

    cout << "*pointer (4): " << *pointer << endl;

    cout << "pointer (4): " << pointer << endl;
    cout << "&pointer (4): " << &pointer << endl;
    cout << endl;

    cout << "x: " << x << endl;
    cout << "&x: " << &x << endl;
    cout << endl;

    cout << "y: " << y << endl;
    cout << "&y: " << &y << endl;
    cout << endl;

    int** doublepointer = &pointer;

    cout << "*doublepointer (1): " << *doublepointer << endl;

    cout << "doublepointer (1): " << doublepointer << endl;

    cout << "&doublepointer (1): " << &doublepointer << endl;
    cout << endl;

    int z = 100;
    *pointer = z;

    cout << "*pointer (5): " << *pointer << endl;

    cout << "pointer (5): " << pointer << endl;

    cout << "&pointer (5): " << &pointer << endl;
    cout << endl;

    cout << "*doublepointer (2): " << *doublepointer << endl;

    cout << "doublepointer (2): " << doublepointer << endl;

    cout << "&doublepointer (2): " << &doublepointer << endl;
    cout << endl;
}

void linkedListInsersationShowCase() {
    Node* head = nullptr;

    insertAtBeginning(head, 3);
    insertAtBeginning(head, 7);
    insertAtBeginning(head, 11);

    cout << "Linked List: ";
    displayList(head);

    Node* current = head;
    while (current != nullptr) {
        if (current->data == 7) {
            insertAfter(current, 5);
            break;
        }
        current = current->next;
    }

    cout << "Linked List after insertion: ";
    displayList(head);
}

void linkedListSearchShowCase() {
    Node* head = nullptr;

    // Insert some elements into the linked list
    insertAtBeginning(head, 67);
    insertAtBeginning(head, -9);
    insertAtBeginning(head, 0);
    insertAtBeginning(head, -55);

    // Display the linked list
    cout << "Linked List: ";
    displayList(head);

    int valueToFind = -9;
    if (search(head, valueToFind)) {
        cout << "Value " << valueToFind << " found in the linked list." << endl;
    }
    else {
        cout << "Value " << valueToFind << " not found in the linked list." << endl;
    }
}

void linkedListDeletionShowCase() {
    Node* head = nullptr;

    insertAtBeginning(head, 5);
    insertAtBeginning(head, 10);
    insertAtBeginning(head, 4);

    cout << "Linked List before deletion: ";
    displayList(head);

    deleteNode(head, 10);

    cout << "Linked List after deletion: ";
    displayList(head);

    deleteTail(head);

    cout << "Linked List after deleting the tail: ";
    displayList(head);
}



int main() {
    pointerShowCase(); // This prints out pointers, refences, and memory address examples
    linkedListInsersationShowCase();//This prints out how a linked list looks before and after inseration
    linkedListSearchShowCase();//This prints a boolean on whether a value in a linked list could be found or not
    linkedListDeletionShowCase();//This prints out how a linked list looks before and after deletion
}