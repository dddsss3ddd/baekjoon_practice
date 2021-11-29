#include <iostream>

using namespace std;

int main() {
    int usrin;
    unsigned long long present_oil_price;
    unsigned long long sx = 0;
    int distance[100000] = { 0 };
    cin >> usrin;


    for (int i = 0; i < usrin - 1; ++i) {
        cin >> distance[i];
    }

    cin >> present_oil_price;
    sx += present_oil_price * distance[0];
    for (int i = 0; i < usrin - 1; ++i) {
        int next_oil_price;
        cin >> next_oil_price;
        if (present_oil_price > next_oil_price) {
            present_oil_price = next_oil_price;
        }
        sx += distance[i + 1] * present_oil_price;
    }
    cout << sx << endl;
}