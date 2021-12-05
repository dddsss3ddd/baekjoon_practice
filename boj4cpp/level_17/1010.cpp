#include <iostream>

using namespace std;
int DP[32][32] = {0};

void Solution(){
    DP[0][0] = 1;
    for(int i=1; i<31; ++i){
        DP[i][0] = 1;
        for(int j=1; j<=i; ++j){
            DP[i][j] = DP[i-1][j] + DP[i-1][j-1];
        }
    }
}

int main(){
    int usrin;
    cin>>usrin;

    Solution();

    // for(int i=0; i<31; ++i){
    //     for(int j=0; j<i; ++j){
    //         cout<<DP[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    int a,b;
    for(int i=0; i<usrin; ++i){
        cin>>a>>b;

        cout<<DP[b][a]<<endl;
    }
}