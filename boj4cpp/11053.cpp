#include <iostream>

using namespace std;

int main(){
    int usrin;
    int dnv[1001][2]={0};
    cin>>usrin;

    int max = 0;
    for(int i=0; i<usrin; ++i){
        cin>>dnv[i][0];
        dnv[i][1] = 1;
        for(int j=0;j<i;++j){
            if(dnv[j][0]<dnv[i][0]){
                if(dnv[j][1]>=dnv[i][1]){
                    dnv[i][1] = dnv[j][1]+1;
                }
            }
        }
        if(dnv[i][1]>max){
            max=dnv[i][1];
        }
    }
    cout<<max<<endl;
}