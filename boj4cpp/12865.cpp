#include <iostream>

using namespace std;

int main(){
    int num,vol;
    cin>>num>>vol;

    int dp[100001] = {0};

    int w,v;
    for(int i=0;i<num;++i){
        cin>>w>>v;
        for(int j=vol;j>=w;--j){
            dp[j] = max(dp[j],dp[j-w]+v);
        }
    }
    cout<<dp[vol]<<endl;
}