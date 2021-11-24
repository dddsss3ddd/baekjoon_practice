#include <iostream>

using namespace std;

int main() {
    int usrin;
    cin >> usrin;
    int arr[1000] = { 0 };
    int inc[1000] = { 0 };
    int dec[1000] = { 0 };
    int mx = 0;
    for (int i = 0; i < usrin; ++i) {
        cin >> arr[i];
        inc[i] = 1;
        dec[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) {
                if (inc[i] <= inc[j]) {
                    inc[i] = inc[j] + 1;
                }
            }
            if (arr[i] < arr[j]) {
                int tmax = max(inc[j], dec[j]);
                if (tmax >= dec[i]) {
                    dec[i] = tmax+1;
                }
            }
        }
        int idmax = max(inc[i], dec[i]);
        if (idmax > mx) {
            mx = idmax;
        }
    }
    cout << mx << endl;
}