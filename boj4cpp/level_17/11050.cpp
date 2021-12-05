#include <iostream>

using namespace std;

int fac(int a){
    if(a <= 2) return a?a:1;
    else return a*fac(a-1);
}

int main(){
    int a,b;

    cin>>a>>b;

    cout<< (fac(a)/fac(b)/fac(a-b))<<endl;
}