#include <iostream>
#include <string>
using namespace std;

int main(){
    while(true){
        int a,b;
        cin>>a>>b;
        if(a==b && b==0) break;

        string res = "neither";
        if(a==0 || b==0){
        }else if(a%b == 0){
            res = "multiple";
        }else if(b%a==0){
            res = "factor";
        }
        cout<<res<<endl;
    }
}