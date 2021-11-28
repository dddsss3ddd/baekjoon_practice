#include <iostream>
using namespace std;

int main(){
    int usrIn;
    int house[1001][3] = {0};
    cin >> usrIn;

    for(int i = 1; i<usrIn+1; ++i){
        cin>>house[i][0]>>house[i][1]>>house[i][2];
    }

    for(int i = 1; i<usrIn+1; ++i){
        house[i][0] += min(house[i-1][1],house[i-1][2]);
        house[i][1] += min(house[i-1][0],house[i-1][2]);
        house[i][2] += min(house[i-1][1],house[i-1][0]);
    }

    cout<<min(min(house[usrIn][0],house[usrIn][1]),house[usrIn][2])<<endl;
}