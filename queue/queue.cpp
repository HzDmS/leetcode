#include<iostream>

using namespace std;


template <typename T>
class Queue {
public:
    Queue(int c = 10);
    ~Queue();
    bool enqueue(T data);
    T dequeue();
    T front();
    bool isEmpty();
    bool isFull();
    int size();
    void info();
private:
    T *queue_;
    int front_;
    int rear_;
    int capacity_;
};

int main() {
    Queue<int> q;
    for (int i = 0; i < 11; i++) {
        q.enqueue(i);
        cout << q.size() << endl;
    }

    for (int j = 0; j < 11; j++) {
        if (!q.isEmpty())
            cout << q.dequeue() << endl;
        else
            break;
    }

    q.info();
    return 0;
}

template<typename T>
Queue<T>::Queue(int c):
    capacity_(c + 1),
    front_(0),
    rear_(0),
    queue_(nullptr) {
        queue_ = new T[c];
        cout << "capacity:" << c << endl;
    }

template <typename T>
Queue<T>::~Queue() {
    if(queue_) {
        delete [] queue_;
    }
}

template <typename T>
bool Queue<T>::isEmpty() {
    return (front_ == rear_);
}

template <typename T>
bool Queue<T>::isFull() {
    return (front_ == ((rear_ + 1) % capacity_));
}

template <typename T>
bool Queue<T>::enqueue(T data) {
    if (isFull()) {
        cout << "current data: " << data << ", queue is full" << endl;
        return false;
    };
    *(queue_ + rear_) = data;
    rear_ = (rear_ + 1) % capacity_;
    return true;
}

template <typename T>
T Queue<T>::dequeue() {
    if (isEmpty()) {
        throw out_of_range("Empty queue!");
    }
    T data = *(queue_ + front_);
    front_ = (front_ + 1) % capacity_;
    return data;
}

template <typename T> 
void Queue<T>::info() {
    cout << "front: " << front_ << ", tail: " << rear_ << endl;
}

template <typename T>
int Queue<T>::size() {
    return (rear_ - front_) % capacity_;
}
