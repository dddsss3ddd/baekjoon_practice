#include <stdio.h>
#include <iostream>

using namespace std;
long long triangle[101] = {0,1,1,1,2,2,3};

void getTriangle(int a){
    triangle[a] = triangle[a-1] + triangle[a-5];
}

int main(){

    for ( int i = 7; i<101; ++i){
        getTriangle(i);
    }

    int testCase;
    cin>>testCase;

    for(int i=0; i<testCase; ++i){
        int test;
        cin>>test;
        cout<< triangle[test]<<endl;
    }

    return 0;
}