/*
A dynamic array implementation in C++.

@author Kamalveer Singh, github.com/kamal-stark-dev
*/

#include <iostream>
#include <utility> // for swap (not actually needed to add here though)
#include <stdexcept> // for out_of_range and invalid_argument errors
using namespace std;

template <typename T>
class DynamicArray {
private:
    int size;
    int capacity;
    T* array;

    void check_index(int index) const {
        if (index < 0 || index >= size)
            throw out_of_range("index out of bounds : /");
    }

    void resize(int new_capacity) {
        T* new_array = new T[new_capacity];

        for (int i = 0; i < size; i++)
            new_array[i] = array[i];

        delete[] array;
        array = new_array;
        capacity = new_capacity;
    }

public:
    DynamicArray(int _capacity) {
        if (_capacity <= 0)
            throw invalid_argument("capacity must be positive : /");

        size = 0;
        capacity = _capacity;
        array = new T[capacity]; // memory allocated on the heap at run-time
    }

    // disabling copy constructor (can't do `DynamicArray arr2 = arr1;`)
    // DynamicArray(const DynamicArray&) = delete;

    // disabling copy assignment operator (can't do `arr2 = arr1;`)
    // DynamicArray& operator=(const DynamicArray&) = delete;

    // copy constructor
    DynamicArray(const DynamicArray& other) : size(other.size), capacity(other.capacity) {
        array = new T[capacity];

        for (int i = 0; i < size; i++)
            array[i] = other.array[i];
    }

    // copy assignment operator

    // DynamicArray& operator=(const DynamicArray& other) {
    //     // self-assignment check
    //     if (this == &other)
    //         return *this;

    //     delete[] array;

    //     size = other.size;
    //     capacity = other.capacity;

    //     array = new int[capacity];

    //     for (int i = 0; i < size; i++)
    //         array[i] = other.array[i];

    //     return *this;
    // }

    // to avoid repeating code
    DynamicArray& operator=(const DynamicArray& other) {
        if (this == &other)
            return *this;

        DynamicArray temp(other);

        swap(size, temp.size);
        swap(capacity, temp.capacity);
        swap(array, temp.array);

        return *this;
    }

    // basic utilities

    int get_size() const {
        return size;
    }

    bool is_empty() const {
        return size == 0;
    }

    const T& get(int index) const {
        check_index(index);
        return array[index];
    }

    void set(int index, T value) {
        check_index(index);
        array[index] = value;
    }

    void add(T value) {
        if (size == capacity)
            resize(capacity * 2);

        array[size++] = value;
    }

    T removeAt(int index) {
        check_index(index);

        T removed_value = array[index];

        for (int i = index; i < size - 1; i++)
            array[i] = array[i + 1];

        size--;

        // optionlly shrink (prevent wastage of space)
        if (size <= (capacity / 4))
            resize(max(1, capacity / 2));

        return removed_value;
    }

    void clear() {
        size = 0;
    }

    void print() const {
        if (size == 0) {
            cout << "[]\n";
            return;
        }
        cout << "[";
        for (int i = 0; i < size; i++)
            cout << array[i] << ", ";

        cout << "\b\b]\n";
    }

    // destructor to free all the memory and prevent leaks
    ~DynamicArray() {
        delete[] array;
    }
};

class Anime {
public:
    string name;
    double rating;

    Anime() : name(""), rating(0.0) {}
    Anime(string s, double r) : name(s), rating(r) {}
};

// operator overloading << to print Anime object
ostream& operator<<(ostream& os, const Anime& anime) {
    os << anime.name << " (" << anime.rating << ")";
    return os;
}

int main() {
    DynamicArray<int> arr(1);

    arr.add(10);
    arr.add(20);
    arr.add(30);

    arr.print();

    cout << "arr[0] = " << arr.get(0) << "\n";

    arr.set(0, 100);
    cout << "arr[0] = " << arr.get(0) << "\n";

    arr.removeAt(1);

    cout << (arr.is_empty() ? "Empty": "Non-Empty") << "\n";

    arr.print();

    // The Rule of Three (check)
    DynamicArray<int> arr2 = arr;

    arr2.set(0, 67);
    cout << "Array 1: ";
    arr.print();

    cout << "Array 2: ";
    arr2.print(); // both arrays will be different as we have created a deep copy

    // Character Array
    DynamicArray<char> char_arr(1);

    char_arr.add('a');
    cout << (char)char_arr.get(0) << "\n";

    char_arr.set(0, '$');
    cout << (char)char_arr.get(0) << "\n";

    // Object Array
    DynamicArray<Anime> anime_arr(3);
    anime_arr.add(Anime("Naruto", 9.7));
    anime_arr.add(Anime("One Piece", 9.7));
    anime_arr.add(Anime("Haikyuu", 9.0));
    anime_arr.add(Anime("One Punch Man", 8.2));
    anime_arr.add(Anime("Death Note", 9.3));

    cout << anime_arr.get(0) << "\n";

    anime_arr.print();

    return 0;
}