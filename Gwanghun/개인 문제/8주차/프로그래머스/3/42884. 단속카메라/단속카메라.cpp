#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*
최소 몇 대의 단속용 카메라가 지나가야 하는가?
브루토프스인가?
그 범위 내에 단속카메라가 있어야만 쓸모가 있음
겹치는 구간들을 찾아야 할 것 같은데 그걸 어떻게하지

겹치는 구간들 찾기 => 해당 구간에 설치 
겹치는 구간이 또 어디 겹치는지.. 그런거 판별 어캐하지 

구간 cnt++해서 겹치는 구간 2 이상인 것들 값 다 넣고 routes에서 그 값들에
포함되어 있으면 
근데 이렇게하면 최소가 안나오지 않나? 여러 구간 측정해버려서 .. 
일단 정렬을 해야될거같은데

첫번째 값 기준 정렬하고 그 값의 종료구간이 시작 구간과 안 겹친다면 cnt++
겹칠때까지 쭉 반복문 돌리기
*/

bool isGreater(vector<int>&v1, vector<int>&v2){
    return v1[1]<v2[1];
}

int cal(vector<vector<int>> routes) {
    
    int cnt=1;
    
    sort(routes.begin(), routes.end(), isGreater);
    
    int firstOne=routes[0][1];
    
    for(int i=1; i<routes.size(); i++){
        if(routes[i][0]>firstOne){
            cnt++;
            firstOne=routes[i][1];
        }
    }
    
    return cnt;
}

int solution(vector<vector<int>> routes) {
    int answer = cal(routes);
    return answer;
}
