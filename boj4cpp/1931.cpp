#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct cftime {
    int start;
    int end;
};

bool gcf(cftime a, cftime b) {
    if (a.start != b.start) {
        if (a.start > b.start) {
            return false;
        }else{
            return true;
        }
    }else {
        if (a.end < b.end) {
            return true;
        }else {
            return false;
        }
    }
}

int main() {
    int usrin;
    cin >> usrin;
    vector<cftime> arr;
    for (int i = 0; i < usrin; ++i) {
        cftime t;
        cin >> t.start >> t.end;
        arr.push_back(t);
    }

    sort(arr.begin(), arr.end(), gcf);

    int res = 1;
    for (int i = arr.size()-1; i >0 ; --i) {
        if (arr[i - 1].end <= arr[i].start) {
            ++res;
        }
        else {
            arr[i - 1] = arr[i];
        }
    }
    cout << res << endl;
}