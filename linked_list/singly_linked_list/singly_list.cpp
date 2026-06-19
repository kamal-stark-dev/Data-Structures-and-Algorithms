#include <iostream>

template <typename T=int>
class Node {
public:
    T data;
    Node* next;

    Node() : data(T()), next(nullptr) {}
    Node(T value) : data(value), next(nullptr) {}
    Node(T value, Node* reference) : data(value), next(reference) {}
};

template <typename T=int>
class SinglyList {
public:
    Node<T> *head;
    Node<T> *tail;
    int len;

    SinglyList() {
        head = tail = nullptr;
        len = 0;
    }

    ~SinglyList() {
        Node<T>* current = head;

        while (current) {
            Node<T>* next = current->next;
            delete current;
            current = next;
        }

        head = tail = nullptr;
        len = 0;
    }

    // Utility - _valid_index

    bool _valid_index(int idx) const {
        if (idx < 0 || idx >= len) return false;
        return true;
    }

    void add(T value) {
        if (!head) {
            head = tail = new Node<T>(value);
            len++;
            return;
        }
        tail->next = new Node<T>(value);
        tail = tail->next;
        len++;
    }

    void insert(int idx, T value) {
        if (idx < 0 || idx > len)
            throw std::out_of_range("Invalid index provided for insertion.");

        if (idx == 0) {
            Node<T>* new_head = new Node<T>(value);
            new_head->next = head;
            head = new_head;
            len++;
            return;
        }
        if (idx == len) {
            // add to end of the list
            add(value); // it also updates the tail
            return;
        }

        Node<T>* temp = head;
        for (int i = 1; i != idx; temp = temp->next, i++)
            ;
        Node<T>* next_node = temp->next;
        temp->next = new Node<T>(value);
        temp->next->next = next_node;
        len++;
    }

    int get_len() const {
        return len;
    }

    T get(int idx) const {
        if (!_valid_index(idx))
            throw std::out_of_range("Invalid index provided for getting value.");

        Node<T>* temp = head;
        for (int i = 0; i != idx; temp = temp->next, i++)
            ;
        return temp->data;
    }

    void set(int idx, T value) {
        if (!_valid_index(idx))
            throw std::out_of_range("Invalid index provided for setting value.");

        Node<T>* temp = head;
        for (int i = 0; i != idx; temp = temp->next, i++)
            ;
        temp->data = value;
    }

    T remove(int idx) {
        if (!_valid_index(idx))
            throw std::out_of_range("Invalid inedex provided for removing value.");

        if (idx == 0) {
            Node<T>* node_to_remove = head;
            T value = head->data;

            if (len == 1)
                head = tail = nullptr;
            else
                head = head->next;

            delete node_to_remove; // free memory
            node_to_remove = nullptr; // clear the pointer to prevent dangling pointers
            len--;
            return value;
        }

        Node<T>* temp = head;
        for (int i = 1; i != idx; temp = temp->next, i++)
            ;
        Node<T>* node_to_delete = temp->next;
        T value = node_to_delete->data;

        temp->next = node_to_delete->next;
        if (node_to_delete == tail) // set tail to temp if the node to delete is the last one
            tail = temp;
        delete node_to_delete;
        node_to_delete = nullptr;
        len--;
        return value;
    }

    void print() const {
        if (!head) {
            std::cout << "List is empty!\n";
            return;
        }

        Node<T> *temp = head;
        while (temp) {
            std::cout << temp->data << "->";
            temp = temp->next;
        }
        std::cout << "NULL\n";
    }
};

int main() {
    SinglyList<int> ll;
    ll.add(10);
    ll.add(20);
    ll.add(40);

    ll.insert(3, 50);

    std::cout << "Len: " << ll.get_len() << "\n";

    ll.set(3, 69);
    std::cout << "ll[3]: " << ll.get(3) << "\n";
    ll.print();

    ll.remove(3);
    std::cout << "Len: " << ll.get_len() << "\n";
    ll.print();

    ll.print();

    return 0;
}