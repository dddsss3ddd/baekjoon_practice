#include <iostream>
#include <map>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=T; t>0; --t){
        int usrin;
        cin>>usrin;

        map<string,int> wear;

        for(int i=0; i<usrin; ++i){
            string a,b;
            cin>>a>>b;
            wear[b]++;
        }
        int res = 1;
        
        for(auto const& v:wear){
            res*=v.second+1;
        }

        cout<<res-1<<endl;
    }
}