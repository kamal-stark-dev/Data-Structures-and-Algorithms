#include <iostream>

template <typename T>
class Node {
public:
    T data;
    Node* prev;
    Node* next;

    Node(): data(T()), prev(nullptr), next(nullptr) {}
    Node(T value): data(value), prev(nullptr), next(nullptr) {}
};

template <typename T>
class DoublyList {
public:
    Node<T>* head;
    Node<T>* tail;
    int len;

    DoublyList() {
        head = tail = nullptr;
        len = 0;
    }

    ~DoublyList() {
        Node<T>* current = head;

        while (current) {
            Node<T>* next = current->next;
            delete current;
            current = next;
        }

        head = tail = nullptr;
        len = 0;
    }

    bool _valid_index(int idx) {
        if (idx < 0 || idx >= len) return false;
        return true;
    }

    void add(T value) {
        if (len == 0) {
            head = tail = new Node<T>(value);
            len++;
            return;
        }

        Node<T>* curr = new Node<T>(value);
        tail->next = curr;
        curr->prev = tail;
        tail = tail->next;
        len++;
    }

    void insert(int idx, T value) {
        if (idx < 0 || idx > len)
            throw std::out_of_range("Provided index is not valid for insertion.");

        if (idx == 0) {
            Node<T>* new_node = new Node<T>(value);
            new_node->next = head;
            head->prev = new_node;
            head = new_node;
            len++;
            return;
        }
        if (idx == len) {
            add(value);
            return;
        }

        Node<T>* curr = head;
        for (int i = 1; i != idx; curr = curr->next, i++)
            ;
        Node<T>* new_node = new Node<T>(value);
        new_node->next = curr->next;
        new_node->prev = curr;
        curr->next->prev = new_node;
        curr->next = new_node;
        len++;
    }

    void set(int idx, T value) {
        if (!_valid_index(idx))
            throw std::out_of_range("Provided index is not valid for setting.\n");

        Node<T>* curr = head;
        for (int i = 0; i != idx; curr = curr->next, i++)
            ;
        curr->data = value;
    }

    T get(int idx) const {
        if (!_valid_index(idx))
            throw std::out_of_range("Provided index is invalid to get.");

        Node<T>* curr = head;
        for (int i = 0; i != idx; curr = curr->next, i++)
            ;
        return curr->data;
    }

    T remove(int idx) {
        if (!_valid_index(idx))
            throw std::out_of_range("Provided index is invalid for deletion.");

        if (idx == 0) {
            Node<T>* node_to_remove = head;
            T value = node_to_remove->data;

            // TODO:

            len--;
            return value;
        }
        if (idx == len - 1) {
            Node<T>* node_to_remove = tail;
            T value = node_to_remove->data;

            // TODO:

            len--;
            return value;
        }

        Node<T>* curr = head;
        for (int i = 1; i != idx; curr = curr->next, i++)
            ;
        Node<T>* node_to_remove = curr->next;
        T value = node_to_remove->data;

        curr->next = node_to_remove->next;
        node_to_remove->next->prev = node_to_remove->prev;

        node_to_remove->prev = nullptr;
        node_to_remove->next = nullptr;
        delete node_to_remove;
        node_to_remove = nullptr;

        len--;
        return value;
    }

    T get_len() const {
        return len;
    }

    void print() const {
        std::cout << "length: " << get_len() << "\n";

        if (len == 0) {
            std::cout << "List is empty.\n";
            return;
        }

        Node<T>* curr = head;
        std::cout << "NULL <-> ";
        while (curr) {
            std::cout << curr->data << " <-> ";
            curr = curr->next;
        }
        std::cout << "NULL\n";
    }
};

int main() {
    DoublyList<int> dll;

    dll.add(10);
    dll.add(20);
    dll.add(30);
    dll.print();

    dll.insert(3, 10);
    dll.print();

    dll.set(3, 69);
    dll.print();

    dll.remove(1);
    dll.print();

    return 0;
}