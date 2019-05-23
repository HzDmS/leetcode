#include<iostream>
#include "stack.h"

using namespace std;

Stack::Stack(int size) :
capacity(size), ptr(0) {
    stack = new int[size];
};

Stack::~Stack() {
    cout << "destructor" << endl;
}

bool Stack::isEmpty() {
    return ptr == 0;
}

bool Stack::isFull() {
    return ptr == capacity;
}

bool Stack::push(int data) {
    if (!isFull()) {
        stack[ptr++] = data;
        return true; 
    }
    return false;
}

int Stack::pop() {
    if (!isEmpty()) {
        int data = stack[--ptr];
        return data;
    }
    throw std::out_of_range("stack is empty!");
}

int Stack::top() {
    if (!isEmpty()) {
        return stack[ptr - 1];
    }
    throw std::out_of_range("stack is empty!");
}

int Stack::size() {
    if (!isEmpty()) return ptr;
    else return 0;
}