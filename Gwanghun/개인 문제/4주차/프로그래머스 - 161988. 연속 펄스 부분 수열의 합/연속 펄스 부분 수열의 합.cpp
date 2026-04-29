#include <vector>
#include <algorithm>

using namespace std;

/*
dp 같긴 함 (값이 일단 너무 큼. 이중 반복문으론 불가)
-> 근데 값을 저장하면서 이전 값을 이용하면서 갈 수 없는 구조 아닌가 ?
그리디?
이거 -1,1 구간 제일 반복 많이 되는 최장길이 부분 수열 구하면 되는 문제 아닌가?
아님 . 그러면 엣지케이스 존재
흠 .. 


-> 케이스는 2가지만 존재 
1. 2가지 케이스의 벡터 형태로 나눔
연속된 값이기 때문에 현재값과 지금까지 펄스 수열의 합 중 큰 값을 dp[현재 위치] 에 저장
2. 그리고 그 위치의 값이 늘 어디가 최대일지는 정해진게 아니기 때문에 늘상 answer은 최댓값으로 갱신
*/

vector<int> one;
vector<int> two;

vector<long long> dp1 (500001);
vector<long long> dp2 (500001);

long long dynamic(){
    
    dp1[0]=(long long)one[0];
    dp2[0]=(long long)two[0];
    long long answer= -1e9;
    
    for(int i=1; i<one.size(); i++) {
        dp1[i]= max((long long)one[i], dp1[i-1]+(long long)one[i]);
        answer=max(answer,dp1[i]);
    }
    
    for(int i=1; i<two.size(); i++){
        dp2[i]= max((long long)two[i], dp2[i-1]+(long long)two[i]);
        answer=max(answer,dp2[i]);
    }
                                   
    return answer;
}

void purse(vector<int>& v, int num){
    for(int i=0; i<v.size(); i++){
        v[i]*=num;
        num*=-1;
    }
}

long long solution(vector<int> sequence) {
    
    if(sequence.size()==1) return max((long long)sequence[0]*-1, (long long)sequence[0]*1);
    
    one=sequence;
    two=sequence;
    
    purse(one,1);
    purse(two,-1);
    
    
    long long answer = dynamic();
    return answer;
}
