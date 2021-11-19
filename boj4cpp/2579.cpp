#include <iostream>
#include <string.h>
using namespace std;

int main(){
    int usrin;
    int stepStack[3][3] = {0};
    int steps[301] = {0};

    cin>>usrin;
    for(int i = 1; i<=usrin; ++i){
        cin>>steps[i];
    }

    stepStack[0][0] = steps[1];
    stepStack[1][1] = steps[1]+steps[2];
    // stepStack[2][0] = steps[1]+steps[3];
    // stepStack[2][2] = steps[1]+steps[2]+steps[3];

    for(int i = 3; i<usrin+1; ++i){
        stepStack[2][0] = max(max(stepStack[0][0],stepStack[0][1]),stepStack[0][2]) + steps[i];
        stepStack[2][1] = stepStack[1][0] + steps[i];
        stepStack[2][2] = stepStack[1][1] + steps[i];

        memcpy(stepStack,stepStack[1],sizeof(int)*3);
        memcpy(stepStack[1],stepStack[2],sizeof(int)*3);
        // memcpy(stepStack[2],stepStack[3],sizeof(int)*3);

        cout<<stepStack[2][0]<<", "<<stepStack[2][1]<<", "<<stepStack[2][2]<<endl;

    }

    int mx = max(max(stepStack[2][0],stepStack[2][1])+steps[usrin-1],stepStack[2][2]) + steps[usrin];

    if(usrin>3)
        cout<<mx<<endl;
    else
        cout<<steps[3]+steps[1]+steps[2]<<endl;

}