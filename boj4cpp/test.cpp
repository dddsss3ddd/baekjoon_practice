#include <stdio.h>
#include <iostream>

using namespace std;

static int flag = 0;

void execCalc(int& a,int& b, const int* opers){

    b = 3;

}


int main(){
    int numCount = 0;
    cin >> numCount;

    int* numbers = (int*)malloc(sizeof(int)*numCount);
    int opers[4] = {0,};
    for(int i = 0; i<numCount; ++i){
        cin>> numbers[i];
    }

    for(int i = 0; i<4; ++i){
        cin>>opers[i];
    }

    int best = 0;
    int worst = 0;
    cout <<best;
    

    return 0;
}