#include <iostream>
#include <string.h>

using namespace std;

int nTriangle[2][501] = {0};

int main(){
    int usrIn;
    cin>>usrIn;

    for(int j = 0; j<usrIn; ++j){
        for(int i = 0; i<j+1; i++){
            cin>>nTriangle[1][i];
            if(i==0){
                nTriangle[1][i] += nTriangle[0][i];
            }else if(i==j){
                nTriangle[1][i] += nTriangle[0][i-1];
            }else{
                nTriangle[1][i] += max(nTriangle[0][i-1],nTriangle[0][i]);
            }
        }
        memcpy(nTriangle,nTriangle[1],sizeof(int)*501);
    }
    int res = 0;
    for(int i =0; i<usrIn+1; ++i){
        if(nTriangle[0][i]>res) res = nTriangle[0][i];
    }
    cout<<res<<endl;
}