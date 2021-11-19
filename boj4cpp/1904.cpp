#include <stdio.h>
#include <iostream>

using namespace std;
int main(){
    int ans[3] = {1,1,2};
    int n;

    cin>>n;
    for(int i = 3; i<n+1;++i){
        ans[0] = (ans[1]+ans[2])%15746;
        ans[1] = ans[2];
        ans[2] = ans[0];

    }
    if(n==2) ans[0]+=1;
    cout<<ans[0]<<endl;
}