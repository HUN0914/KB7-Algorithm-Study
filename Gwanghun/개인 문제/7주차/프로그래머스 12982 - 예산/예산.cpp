#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int cal(vector<int> d, int budget) {
   int result =0; 
    
    sort(d.begin(),d.end());
    for(int i=0; i<d.size(); i++){
        if(budget-d[i]>=0) {
            budget-=d[i];
            result++;
        }
    }
    
    return result;
}

int solution(vector<int> d, int budget) {
    int answer = cal(d,budget);
    return answer;
}