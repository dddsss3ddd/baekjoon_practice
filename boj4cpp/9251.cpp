/*
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
*/

#include <iostream>

using namespace std;

int main(){
    string a ;
    string b ;
    int mp[2][1001] = {0};

    int* post = mp[1];
    int* pre = mp[0];
    int* temp = nullptr;
    cin >> a >>b;
    int la,lb;
    la = a.length();
    lb = b.length();

    for(int i = 1; i<=lb; ++i){
        for(int j=1; j<=la; ++j){
            if(b[i-1]==a[j-1]){
                post[j] = pre[j-1]+1;
            }else{
                post[j] = max(post[j-1],pre[j]);
            }
        }
        temp = pre;
        pre = post;
        post = temp;
    }
    cout<<pre[la]<<endl;
}