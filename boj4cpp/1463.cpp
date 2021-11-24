#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int usrin;
    cin >> usrin;
    int arr[1000001] = { 0 };
    arr[0] = -1;

    for (int i = 1; i <= usrin; ++i) {
        arr[i] = arr[i - 1] + 1;
        if (!(i & 1)) {
            arr[i] = min(arr[i], arr[i / 2] + 1);
        }
        if (i / 3 == 0) {
            arr[i] = min(arr[i], arr[i / 3] + 1);
        }
    }
    cout << arr[usrin] << endl;
}