#include <iostream>

using namespace std;

int main(){
    int a,b;
    cin>>a>>b;
    int gdc_a=a,gdc_b=b,gdc_r=1;
    int mnmulti = 0;
    int r=1;
    while(gdc_r != 0){
        gdc_r = gdc_a%gdc_b;
        gdc_a = gdc_b;
        gdc_b = gdc_r;
    }
    
    cout<<gdc_a<<"\n"<<(a*b/gdc_a)<<endl;
}