#include<iostream>
#include<chrono>

using namespace std;
using namespace std::chrono;


class Node {
public:
    Node(int);
    int data;
    Node* next;
};

void push(Node**, int);
void printLinkedList(Node*);
void frontEndSplit(Node*, Node**, Node**);
void MergeSort(Node**);
Node* Merge(Node*, Node*);

int main() {

    Node* head = nullptr;
    push(&head, 1);
    push(&head, 2);
    push(&head, 3);
    push(&head, 4);
    push(&head, 5);
    push(&head, 6);
    push(&head, 7);
    printLinkedList(head);
    
    //Node* a = nullptr;
    //Node* b = nullptr;

    //frontEndSplit(head, &a, &b);
    //printLinkedList(a);
    //printLinkedList(b);

    MergeSort(&head);
    printLinkedList(head);
    
    return 0;
}

void push(Node** headref, int newData) {
    Node* newNode = new Node(newData);
    newNode -> next = *headref;
    *headref = newNode;
}

Node::Node(int data) {
    this -> data = data;
    next = nullptr;
}

void printLinkedList(Node* head) {
    while (head) {
        cout << head -> data << " ";
        head = head -> next;
    }
    cout << endl;
}

void frontEndSplit(Node* head, Node** frontref, Node** backref) {

    Node* slow = head;
    Node* fast = head -> next;

    while (fast) {
        fast = fast -> next;
        if (fast) {
            fast = fast -> next;
            slow = slow -> next;
        }
    }

    *frontref = head;
    *backref = slow -> next;
    slow -> next = nullptr;
}

Node* Merge(Node* a, Node* b) {

    if (a == nullptr)
        return (b);
    if (b == nullptr)
        return (a);

    Node* head = nullptr;
    if (a -> data < b -> data) {
        head = a;
        head -> next = Merge(a -> next, b);
    }else {
        head = b;
        head -> next = Merge(a, b -> next);
    }

    return (head);
}

void MergeSort(Node** headref) {
    Node* head = *headref;
    if (head == nullptr || head -> next == nullptr) {
        return;
    }
    
    Node* a = nullptr;
    Node* b = nullptr;

    frontEndSplit(head, &a, &b);
    MergeSort(&a);
    MergeSort(&b);

    *headref = Merge(a, b);
}
