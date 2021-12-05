#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int usrin;
    int factors[50] = {0};

    cin>>usrin;

    for(int i=0; i<usrin;++i){
        cin>>factors[i];
    }
    sort(factors,factors+usrin);
    
    cout<<(factors[0]*factors[usrin-1])<<endl;
}