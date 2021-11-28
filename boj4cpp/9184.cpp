#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

bool ansmap[21][21][21] = {false,};
int ans[21][21][21] = {1,};

int getValue(const int& a,const int& b,const int& c){

    if(a<= 0 || b<= 0 ||c<= 0){
        return 1;
    }else if(a>20 || b>20 || c>20){
        return getValue(20,20,20);
    }else if(ansmap[a][b][c]){ return ans[a][b][c];
    }else if(a == 0 || b== 0 || c== 0){
        return 1;
    }else if(a<b && b<c){
        ans[a][b][c] = getValue(a,b,c-1)+getValue(a,b-1,c-1)-getValue(a,b-1,c);
        ansmap[a][b][c] = true;
        return ans[a][b][c];
    }else{
        ans[a][b][c] = getValue(a-1,b,c)+getValue(a-1,b-1,c) + getValue(a-1,b,c-1) - getValue(a-1,b-1,c-1);
        ansmap[a][b][c] = true;
        return ans[a][b][c];
    }
}

int main(){
    for(int i = 0; i<21; ++i){
        for (int j=0; j<21; ++j){
            for(int k=0; k<21; ++k){
                getValue(i,j,k);
            }
        }
    }

    int a,b,c;

    while(true){
        cin>>a>>b>>c;

        if(a==-1 && b==-1 && c==-1) break;
        printf("w(%d, %d, %d) = %d\n",a,b,c,getValue(a,b,c));
    }
}