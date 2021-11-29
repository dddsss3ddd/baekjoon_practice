#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int usrin;
    cin >> usrin;

    int mins[1000] = { 0 };

    for (int i = 0; i < usrin; ++i) {
        cin >> mins[i];
    }

    sort(mins, mins + usrin);

    int sx = 0;

    for (int i = 0; i < usrin; ++i) {
        sx += mins[i] * (usrin - i);
    }
    cout << sx << endl;
}