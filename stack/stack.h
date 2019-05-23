#ifndef _STACK_H_
#define _STACK_H_

class Stack{
    public:
        Stack(int size);
        ~Stack();
        bool push(int data);
        int pop();
        int size();
        bool isEmpty();
        bool isFull();
        int top();
    private:
        int capacity;
        int* stack;
        int ptr;
};

#endif