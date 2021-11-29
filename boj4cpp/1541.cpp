#include <iostream>
#include <string>

using namespace std;

int main() {
    string usrin;

    cin >> usrin;
    usrin.push_back('+');

    cout << usrin << endl;

    int sx = 0;
    int idx_s = 0;
    int idx_e = 0;
    bool find_minus = false;
    for (int i = 0; i < usrin.length(); ++i) {
        if (usrin[i] == '+' || usrin[i] == '-') {
            idx_e = i;
            cout << "start index = " << idx_s << ", end index=" << idx_e <<", string = "<<usrin.substr(idx_s,idx_e) << endl;
            if (find_minus) {
                cout << "m string num = " << usrin.substr(idx_s, idx_e) << endl;
                sx -= stoi(usrin.substr(idx_s, idx_e));
            }else {
                cout << "p string num = " << usrin.substr(idx_s, idx_e) << endl;
                sx += stoi(usrin.substr(idx_s, idx_e));
                if (usrin[i] == '-') {
                    find_minus = true;
                }
            }
            idx_s = i + 1;
        }
    }

    cout << sx << endl;

}