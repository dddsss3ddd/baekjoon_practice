#include <iostream>

#define DV 10007

int N = 1000;
int K = 1000;
int DP[1010][1010];
int gcd(int a,int b){return b? gcd(b,a%b):a;}

void Solution()
{
 
    for (int i = 1; i <= N; i++)
    {
        for (int j = 0; j <= K; j++)
        {
            if (j == 0) DP[i][j] = 1;
            else if (i == j) DP[i][j] = 1;
            else DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j];
 
            DP[i][j] = DP[i][j] % DV;
        }
    }
}



using namespace std;

int main(){
    Solution();

    int a,b;
    int v[1001] = {0};
    a = 1; b=0;
    while(true){

        
        // cin>>a>>b;
        

        for(int i=0; i<=a; ++i){
            if(i<=b) v[i] = 1;
            else v[i] = i;
        }

    for(int i=2; i<=a-b; ++i){
        int dev = i;
        for(int j=b+1; j<=a; ++j){
            if(v[j]%dev==0){
                v[j] /= dev;
                break;
            }else{
                int gcdv = gcd(v[j],dev);
                if(gcdv != 1){
                    v[j] /= gcdv;
                    dev /= gcdv;
                }
            }
        }
    }

        int res = 1;

        for(int i=b+1; i<=a; ++i){
            res = res*v[i]%DV;
        }
        // cout<<res<<endl;

        if(res != DP[a][b]){
            cout<<"not same.a,b="<<a<<","<<b<<" res="<<res<<", DP="<<DP[a][b]<<endl;
            break;
        }else{
            cout<<"a="<<a<<", b="<<b<<" ok"<<endl;
        }
        if(++b>a){
            ++a;
            b=0;
            if(a>1000) break;
        }
    }
}