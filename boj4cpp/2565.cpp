#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    int usrin;
    int A[500] = { 0 };
    int B[100] = {0};
    int C[100] = {0};

    cin>>usrin;

    for (int i =0; i<usrin;++i){
        int a,b;
        cin>>a>>b;
        A[a-1]=b;
    }
    int idx = -1;
    for(int i=0; i<500;++i){
        if(A[i] != 0){
            B[++idx]=A[i];
        }
        if(idx == usrin-1){ break;}    
    }
    int mx = 0;
    for(int i=0; i<usrin;++i){
        C[i] = 1;
        for(int j=0; j<i; ++j){
            if(B[i]>B[j] && C[i] <= C[j]){
                C[i] = C[j] +1;
            }
        }
        mx = mx<C[i]?C[i]:mx;
    }
    cout<<(usrin-mx)<<endl;
}