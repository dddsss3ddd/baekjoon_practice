#include <iostream>

using namespace std;

int gcd(int a,int b){
    return b? gcd(b,a%b):a;
}

int main(){
    int usrin,origin;

    cin>>usrin>>origin;

    for(int i=0; i<usrin-1; ++i){
        int next;
        cin>>next;
        int t_gcd = gcd(origin,next);
        cout<<(origin/t_gcd)<<"/"<<(next/t_gcd)<<endl;
    }
}