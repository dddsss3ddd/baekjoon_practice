#include <iostream>

using namespace std;

int paper[128][128];

int* dcf(int size, int x, int y) {
    bool same = true;
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (paper[x][y] != paper[x + i][y + j]) {
                same = false;
                break;
            }
        }
        if (!same) {
            break;
        }
    }

    int* res = (int*)malloc(sizeof(int) * 2);
    res[0] = 1;
    res[1] = 0;

    if (!same) {
        int nsize = size / 2;
        int* part_a = dcf(nsize, x + nsize, y + nsize);
        int* part_b = dcf(nsize, x, y + nsize);
        int* part_c = dcf(nsize, x + nsize, y);
        int* part_d = dcf(nsize, x, y);

        res[0] = part_a[0] + part_b[0] + part_c[0] + part_d[0] ;
        res[1] = part_a[1] + part_b[1] + part_c[1] + part_d[1];

        delete[] part_a, part_b, part_c, part_d;
    }else {
        if (paper[x][y] != 0) {
            res[0] = 0;
            res[1] = 1;
        }
    }
    return res;
}


int main() {
    int usrin;
    cin >> usrin;

    for (int i = 0; i < usrin; ++i) {
        for (int j = 0; j < usrin; ++j) {
            cin >> paper[i][j];
        }
    }

    int* res = dcf(usrin, 0, 0);

    cout << res[0] << endl; //white
    cout << res[1] << endl; //blue

    delete[] res;

}