#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int numCount = 0;
    cin >> numCount;
    vector<int> operVec;
    int* numbers = (int*)malloc(sizeof(int)*numCount);
    int opers = 0;

    int min = 0;
    int max = 0;    
    for(int i = 0; i<numCount; ++i){
        cin>> numbers[i];
    }


    for(int i = 1; i<5; ++i){
        cin>>opers;
        // cout<< opers <<endl;
        for(int j = 0; j<opers; ++j){
            operVec.push_back(i);
        }
    }
    // cout<< operVec[0] <<endl;

    int a = numbers[0];
    for(int i = 0; i<numCount-1; ++i){
        if(operVec[i] == 1){
            a+=numbers[i+1];
        }else if(operVec[i] == 2){
            a-=numbers[i+1];
        }else if(operVec[i] == 3){
            a*=numbers[i+1];
        }else{
            a/=numbers[i+1];
        }
    }
    min = a;
    max = a;

    while(next_permutation(operVec.begin(),operVec.end())){
        int t = numbers[0];
        for(int i = 0; i<numCount-1; ++i){
            if(operVec[i] == 1){
                t+=numbers[i+1];
            }else if(operVec[i] == 2){
                t-=numbers[i+1];
            }else if(operVec[i] == 3){
                t*=numbers[i+1];
            }else{
                t/=numbers[i+1];
            }
        }



        if(t>max){
            max = t;
        }
        if(t<min){
            min = t;
        }
    }

    cout<<max <<endl;
    cout<<min <<endl;

    return 0;
}