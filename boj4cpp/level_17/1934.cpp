#include <iostream>

using namespace std;

int gdc(int a, int b){
    int ga,gb,gc;
    ga = a;
    gb = b;
    gc = 1;
    while(gc != 0){
        gc = ga%gb;
        ga = gb;
        gb = gc;
    }
    return a*b/ga;
}

int main(){
    int usrin;
    cin>>usrin;

    int a[1000],b[1000];
    for(int i=0; i<usrin; ++i){
        cin>>a[i]>>b[i];
    }
    for(int i=0; i<usrin;++i){
        cout<<gdc(a[i],b[i])<<endl;
    }
}