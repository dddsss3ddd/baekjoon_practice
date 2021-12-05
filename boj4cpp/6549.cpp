//Not solved!!!

#include <iostream>

#include <stack>

using namespace std;

int main() {
    int usrin;
    cin >> usrin;
    while (usrin != 0) {
        stack<int> k;
        int mx = 0;

        for (int j = 0; j < usrin; ++j) {
            int t;
            cin >> t;
            int v;
            for (int i = 1; i <= k.size(); ++i) {
                if (k.top() > t) {
                    v = k.top();
                    if (mx < i* v) {
                        mx = i * v;
                        k.pop();
                    }
                }
                else {
                    k.push(t);
                    break;
                }
            }
        }
        if (!k.empty()) {
            int v;
            for (int i = 1; i <= k.size(); ++i) {
                v = k.top();
                if (mx < i * v) {
                    mx = i * v;
                    k.pop();
                }
            }
        }
        cout << mx << endl;
        cin >> usrin;
    }
}