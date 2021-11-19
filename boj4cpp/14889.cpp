#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main(){
    int people = 0;
    cin >> people;

    int ** stats = new int*[people];
    for( int i = 0 ; i< people; ++i){
        stats[i] = new int[people];
        for(int j = 0; j<people; ++j){
            cin>>stats[i][j];
        }
    }

    vector<int> teamMate;

    for(int i = 0; i<people; ++i){
        if(i<people/2){
            teamMate.push_back(0);
        }else{
            teamMate.push_back(1);
        }
    }

    int min = 200000000;
    do{
        vector<int> teamA;
        vector<int> teamB;
        for(int i= 0; i<people; ++i){
            if(teamMate[i] == 0){
                teamA.push_back(i);
            }else{
                teamB.push_back(i);
            }
        }

        int teamARate = 0;
        int teamBRate = 0;

        for (size_t i = 0; i < people/2; i++)
        {
            for (size_t j = i+1; j < people/2; ++j)
            {
                teamARate += stats[teamA[i]][teamA[j]] + stats[teamA[j]][teamA[i]];
                teamBRate += stats[teamB[i]][teamB[j]] + stats[teamB[j]][teamB[i]];
            }
        }

        int diff = abs(teamARate-teamBRate);
        if(diff==0){
            cout<<0<<endl;
            return 0;
        }else{
            min = diff<min?diff:min;
        }

    }while(next_permutation(teamMate.begin(),teamMate.end()));

    cout<<min<<endl;


}