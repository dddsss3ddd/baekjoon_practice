#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int fgcd(int a,int b){
    return b? fgcd(b,a%b):a;
}

int main(){
    int usrin ;
    cin>>usrin;

    int nums[100] = {0};

    for(int i=0; i<usrin; ++i){
        cin>>nums[i];
    }

    sort(nums,nums+100,greater<int>());

    int vgdc = nums[0]-nums[1];

    for(int i=1; i<usrin-1; ++i){
        vgdc = fgcd(vgdc,nums[i]-nums[i+1]);
    }

    vector<int> res_a;
    vector<int> res_b;
    res_b.push_back(vgdc);

    int lim = sqrt(vgdc);
    int limp = lim;
    if(lim*lim != vgdc){
        ++limp;
    }

    for(int i=2; i<limp;++i){
        if(vgdc%i==0){
            res_a.push_back(i);
            res_b.push_back(vgdc/i);
        }
    }
    if(vgdc==lim*lim){
        res_a.push_back(lim);
    }

    for(int i=0; i<res_a.size();++i){
        cout<<res_a[i]<<" ";
    }
    for(int i=res_b.size()-1; i>=0;--i){
        cout<<res_b[i]<<" ";
    }

    cout<<endl;

}