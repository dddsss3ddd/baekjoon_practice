// #include <iostream>

// using namespace std;
// int main(){
//     int usrin;

//     int arr[2] = {0};

//     int * a= arr;
//     int *b = arr +1;

//     cin>>usrin;
    
//     int mx = -1000;
//     bool sw = true;

//     for(int i =0; i<usrin; ++i){
//         cin>>*b;
//         if(*a > 0){
//             *b += *a;
//         }
//         if(mx<*b){
//             mx = *b;
//         }
//         if(sw){
//             a+=1;
//             b-=1;
//             sw = false;
//         }else{
//             a-=1;
//             b+=1;
//             sw = true;
//         }
//     }
//     cout<<mx<<endl;
// } //2020kb, 28ms

#include <iostream>

using namespace std;

int main(){
    int usrin;
    int numbers[100001] = {0};
    int mx = -1000;
    cin>>usrin;

    for(int i=1; i<=usrin; ++i){
        cin>>numbers[i];
        if(numbers[i-1]>0){
            numbers[i]+= numbers[i-1];
        }
        if(mx<numbers[i]){
            mx = numbers[i];
        }
    }
    cout<<mx<<endl;
}