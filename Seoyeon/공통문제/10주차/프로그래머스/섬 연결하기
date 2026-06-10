#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parent;

// 경로 압축
// 1. 재귀로 루트 노드를 찾음.
// 2. 찾는 과정에서 만난 모든 노드의 부모를 루트로 바꿔줌.
int findParent(int x){
    if(parent[x] == x) return x;
    return parent[x] = findParent(parent[x]);
}

// 두 집합 합치기
void unionParent(int a, int b){
    a = findParent(a);
    b = findParent(b);
    
    // 그냥 두 집합 합치는 것임(큰 의미 x...보기 편하려고~ㅡ~더 작은 값을 부모로 함.)
    if(a < b){
        parent[b] = a;
    }
    else{
        parent[a] = b;
    }
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    // 부모 초기화
    parent.resize(n);
    for(int i = 0; i < n; i++){
        parent[i] = i;
    }
    
    // 비용 기준 오름차순 정렬
    sort(costs.begin(), costs.end(),[](vector<int> &a, vector<int> &b){
        return a[2] < b[2];
    });
        
    // 크루스칼
    for(auto& cost : costs){
        int a = cost[0];
        int b = cost[1];
        int c = cost[2];
        
        // 사이클이 생기지 않을 때만 연결
        // findParent(a) == findParent(b)면 a와 b는 이미 같은 그룹!(사이클됨.)
        if(findParent(a) != findParent(b)){
            unionParent(a, b);
            answer += c;
        }
    }
    
    return answer;
}
