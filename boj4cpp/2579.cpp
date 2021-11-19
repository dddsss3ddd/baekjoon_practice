#include <iostream>
#include <string.h>
using namespace std;

int main(){
    int usrin;
    int stepStack[3][2] = {0};
    int steps[301] = {0};

    cin>>usrin;
    for(int i = 1; i<=usrin; ++i){
        cin>>steps[i];
    }

    int step_val[3][2] = {0};

    step_val[0][0] = steps[1];
    step_val[1][0] = steps[2];
    step_val[1][1] = steps[1] + steps[2];

    //3보다 작은 값 출력을 위해 미리 값을 넣어둔다.
    memcpy(step_val[2],step_val[1],sizeof(int)*2);

    // cout<<step_val[0][0]<<","<<step_val[0][1]<<endl;
    // cout<<step_val[1][0]<<","<<step_val[1][1]<<endl;

    for(int i= 3; i<=usrin; ++i){
        step_val[2][0] = max(step_val[0][0],step_val[0][1]) + steps[i];//13
        step_val[2][1] = step_val[1][0]+steps[i];//15

        //값을 하나씩 민다.
        memcpy(step_val[0],step_val[1],sizeof(int)*2);
        memcpy(step_val[1],step_val[2],sizeof(int)*2);
        // cout<<step_val[1][0]<<","<<step_val[1][1]<<"         steps[i]="<<steps[i]<<endl;
    }

    // cout<<"fin=max("<<step_val[2][0]<<","<<step_val[2][1]<<")"<<endl;
    cout<<max(step_val[2][0],step_val[2][1])<<endl;
}