#include <iostream>

using namespace std;

int main(){
    int k,aim;
    int coin[10] = {1,1,1,1,1,1,1,1,1,1};
    int res = 0;
    cin>>k>>aim;

    for(int i=k-1; i>=0; --i){
        cin>>coin[i];
    }
    for(int i=0; i<k;++i){
        res += aim/coin[i];
        aim = aim%coin[i];
    }
    cout<<res<<endl;
}