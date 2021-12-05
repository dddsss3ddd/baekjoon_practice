#include <iostream>

#define DV 10007

using namespace std;

int gcd(int a,int b){return b? gcd(b,a%b):a;}

int main(){
    int a,b;
    int v[1001] = {0};
    cin>>a>>b;

    for(int i=0; i<=a; ++i){
        if(i<=b) v[i] = 1;
        else v[i] = i;
    }
    // for(int i=0; i<=a; ++i){
    //     cout<<v[i]<<" ";
    // }
    // cout<<endl;

    for(int i=2; i<=a-b; ++i){
        int dev = i;
        for(int j=b+1; j<=a; ++j){
            if(v[j]%dev==0){
                v[j] /= dev;
                break;
            }else{
                int gcdv = gcd(v[j],dev);
                if(gcdv != 1){
                    v[j] /= gcdv;
                    dev /= gcdv;
                }
            }
        }
    }

    // for(int i=0; i<=a; ++i){
    //     cout<<v[i]<<" ";
    // }
    // cout<<endl;

    int res = 1;

    for(int i=b+1; i<=a; ++i){
        res = res*v[i]%DV;
        // cout<<"mul res="<<res<<", v[i]="<<v[i]<<endl;
    }
    cout<<res<<endl;
}