#include <iostream>

using namespace std;

#define MODULER 1000000000

int main(){
    int usrin;
    cin >> usrin;

    int endDigit1[10] = { 0,1,1,1,1,1,1,1,1,1 };
    int endDigit2[10] = { 0,1,1,1,1,1,1,1,1,1 };

    int* base = endDigit1;
    int* point = endDigit2;
    for (int i = 2; i <= usrin; ++i) {
        if (i & 1) {
            point = endDigit1;
            base = endDigit2;
        }
        else {
            point = endDigit2;
            base = endDigit1;
        }
        for (int j = 1; j < 9; ++j) {
            point[j] = (base[j - 1] + base[j + 1])%MODULER;
        }
        point[0] = base[1] % MODULER;
        point[9] = base[8] % MODULER;
    }
    int sum = point[0];
    for (int i = 1; i < 10; ++i) {
        sum += point[i];
        sum %= MODULER;
    }

    cout << sum << endl;
}