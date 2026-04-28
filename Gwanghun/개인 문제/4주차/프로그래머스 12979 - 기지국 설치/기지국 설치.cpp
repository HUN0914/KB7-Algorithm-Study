#include <iostream>
#include <vector>
using namespace std;

/*
양옆 W칸만큼 전파 
dfs -> 아파트 개수 N (O(n)으로 끝내야 할 범위)
DP X -> 그리디 -> 근데 양 옆 전파는 어떻게 처리?
1. 기존 있는 전파범위 다 제외 bool visited
2. 처음부터 시작해서 처음+w 
pointer + 그리디

반복문 처음부터 w만큼 이동하고 만약 이 사이에서 다 false일 경우
-> bool이라해도 200 000 000 만큼 선언해줄 수 있나?
-> 
station + - 로 구간 각각 다 나누고 거기서 딱 최적의 개수만큼 계산
최적의 수 구하는 법 처음, 마지막엔 한쪽 끝만 된다는 것을 고려
근데 기존에 주어진 것 중에서 겹치는 경우엔 어떻게 생각 ?

*/

struct point{
    int start;
    int end;
};

vector<point> pointes;

int cal(int n, vector<int> stations, int w){
   
    int range= 2*w+1;
    
    // 근데 기존에 주어진 것 중에서 겹치는 경우엔 어떻게 생각 ?
    // 직전 location 값 기준으로 뭐 하면 될거같긴한데..
    // 맨 처음에만 왼쪽 값 다 담아주고 맨 마지막에만 오른쪽 다 값 담아주고 중간은 늘 오른쪽 단위로만 체크하기
    
    if(1<stations[0]-w){
        pointes.push_back({1, stations[0]-w-1});
    }
    
    for(int i=0; i<stations.size()-1; i++){
        int value = stations[i];
        int nextValue = stations[i+1];
        
        int start = value+w+1;
        int end = nextValue-w-1;
        
        if(start<=end){
            pointes.push_back({start, end});
        }
    }
    
    if(stations.back()+w<n){
        pointes.push_back({stations.back()+w+1, n});
    }
    
    int total=0;
    
    for(int i=0; i<pointes.size(); i++){
        int length=pointes[i].end-pointes[i].start+1;
        total+=(length+range-1) / range;
    }
    
    return total;
}

int solution(int n, vector<int> stations, int w)
{
    int answer = cal(n,stations,w);

    return answer;
}
