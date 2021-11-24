#include <iostream>

using namespace std;

int main() {

    int usrin;
    cin >> usrin;

    int vals[4][2] = {0};

    int* past = vals[0];
    int* before = vals[1];
    int* present = vals[2];
    int* future = vals[3];
    int* temp = nullptr;
    

    int wine;
    for (int i = 0; i < usrin; ++i) {
        cin >> wine;
        future[0] = max(max(past[0], past[1]), max(before[0], before[1])) + wine;
        future[1] = present[0] + wine;

        temp = past;
        past = before;
        before = present;
        present = future;
        future = temp;

    }

    cout << max(max(before[0],before[1]),max(present[0],present[1])) << endl;

}