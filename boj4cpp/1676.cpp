#include <iostream>

using namespace std;

int main() {
    int usrin;
    int res = 0;
    cin >> usrin;
    for (int i = 1; i <= usrin; ++i) {
        if (i % 500 == 0 || i%125==0) {
            res += 3;
        }else if (i % 100 == 0 || i%25 == 0) {
            res += 2;
        }else if (i % 10 == 0 || i % 10 == 5) {
            res += 1;
        }
    }
    cout << res << endl;
}