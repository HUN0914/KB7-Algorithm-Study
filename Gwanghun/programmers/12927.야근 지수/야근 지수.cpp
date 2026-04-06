#include <string>
#include <vector>
#include <queue>

using namespace std;

long long minPQ(int n, vector<int> works){
    long long total=0;
    
    priority_queue<int> pq;
    
    int sum=0;
    for(auto & val : works) sum+=val;
    
    if(sum<=n) return 0;
    
    for(auto & val : works) pq.push(val);
    
    while(n--){
        int val=pq.top();
        pq.pop();
        val--;
        pq.push(val);
    }
    
    while(!pq.empty()){
        total+= pq.top()*pq.top();
        pq.pop();
    }
    
    return total;
}

long long solution(int n, vector<int> works) {
    long long answer = 0;
    answer=minPQ(n, works);
    
    return answer;
}
