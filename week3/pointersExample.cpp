#include <iostream>
using namespace std;

int main(){

    int x = 10;

    int *pointer = &x;

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

    int **doublepointer = &pointer;

    cout << "*doublepointer (1): " << *doublepointer << endl;

    cout << "doublepointer (1): " << doublepointer << endl;

    cout << "&doublepointer (1): " << &doublepointer << endl;
    cout << endl;

    int z = 100;
    *pointer = z;

    cout << "*doublepointer (2): " << *doublepointer << endl;

    cout << "doublepointer (2): " << doublepointer << endl;

    cout << "&doublepointer (2): " << &doublepointer << endl;
    cout << endl;

    cout << "*pointer (5): " << *pointer << endl;

    cout << "pointer (5): " << pointer << endl;

    cout << "&pointer (5): " << &pointer << endl;
    cout << endl;
}