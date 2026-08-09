#include <iostream>

class Node {
public:
  int data;
  Node* next;

  Node() : data(0), next(nullptr) {}
  Node(int val) : data(val), next(nullptr) {}
  Node(int val, Node* next_) : data(val), next(next_) {}
};

class SinglyCircularList {
public:
  Node head;
  Node tail;
};

int main() {
  SinglyCircularList scl;
}
