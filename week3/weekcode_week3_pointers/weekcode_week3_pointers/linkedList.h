#pragma once

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>

struct Node {
    int data;
    Node* next;
};

void insertAtBeginning(Node*& head, int newData); //This function allows us to insert new nodes at the head of the linked list

void insertAfter(Node* prevNode, int newData);//This function inserts nodes at specific places in the linked list

void displayList(Node* head);//This function iterates over the linked list, printing each value

bool search(Node* head, int value);//This function returns a boolean on whether a value exists in the linked list or not

void deleteNode(Node*& head, int key);//This function deletes nodes at specific places in the linked list

void deleteTail(Node*& head);//This function deletes the tail of the linked list

#endif
